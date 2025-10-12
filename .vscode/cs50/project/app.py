from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from functools import wraps
from dotenv import load_dotenv
import os
from transformers import pipeline

app = Flask(__name__)

generator = pipeline("text2text-generation", model="google/flan-t5-base", framework="pt")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# -------------------
# Helper functions
# -------------------
def get_db():
    conn = sqlite3.connect("project.db")
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    """Decorate routes to require login."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

def apology(message, code=400):
    """Render message in apology template."""
    def escape(s):
        for old, new in [
            ("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
            ("%", "~p"), ("#", "~h"), ("/", "~s"), ('"', "''")
        ]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

# -------------------
# Routes
# -------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        language = request.form.get("language")
        country = request.form.get("country")
        skills = request.form.getlist("skills")

        if not username:
            return apology("Username is required", 400)
        if not password:
            return apology("Password is required", 400)
        if password != confirm:
            return apology("Passwords do not match", 400)

        conn = get_db()
        user_exists = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user_exists:
            conn.close()
            return apology("Username already take", 400) 
               
        hashed_pw = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, password_hash, language, country, skills) VALUES (?, ?, ?, ?, ?)", 
            (username, hashed_pw, language, country, ",".join(skills))
        )
        conn.commit()

        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        session["user_id"] = user["id"]
        conn.close()
        return redirect(url_for("account"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.clear()  

        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return render_template("login.html", message="Username is required")
        if not password:
            return render_template("login.html", message="Password is required")

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username= ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]   # for screen certifing you are login
            print("DEBUG session:", dict(session))   # checking session. printing on the terminal
            return redirect(url_for("account"))  
        else:
            return render_template("login.html", message="Invalid username or password")
        
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# account function (app.py)
@app.route("/account")
@login_required
def account():
    # Get user_id from the session
    user_id = session.get("user_id")
    if not user_id:
        # 세션이 없으면 /login으로 보내거나 에러 처리
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    # Get the account info from the user_id
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    print("DEBUG account - fetched user:", dict(user) if user else None)
    if not user:
        conn.close()
        return apology("User not found", 400)

    # Get the Project info from the user db
    cur.execute("SELECT * FROM ideas WHERE user_id = ?", (user_id,))
    ideas = cur.fetchall()
    project_count = len(ideas)

    # Get the notifications count info
    cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id = ?", (user_id,))
    notifications_count = cur.fetchone()[0]
    print("DEBUG account - notifications_count:", notifications_count)

    conn.close()

    # If there is no user in the DB / safe protocol 
    if not user:
        return apology("User not found", 400)

    # Send data to the account.html
    return render_template(
        "account.html",
        user=user,
        ideas=ideas,
        project_count=project_count,        
        notifications_count=notifications_count,
    )


@app.route("/idea", methods=["GET", "POST"])
@login_required
def idea():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        # 1. 폼 데이터 가져오기
        title = request.form.get("title")
        problem = request.form.get("problem")
        concept = request.form.get("concept")
        workflow = request.form.get("workflow")  # optional
        team_members = request.form.getlist("team_members")  # 체크박스 여러 개
        project_style = request.form.get("project_style")

        # 2. 필수 항목 검증
        if not title or not problem or not concept or not team_members or not project_style:
            conn.close()
            return render_template("idea.html", message="Please fill in all required fields")

        # 3. team_members는 콤마로 연결
        team_members_str = ",".join(team_members)

        # 4. DB에 삽입
        cur.execute(
            "INSERT INTO ideas (user_id, title, problem, concept, workflow, team_members, project_style) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (session["user_id"], title, problem, concept, workflow, team_members_str, project_style)
        )
        conn.commit()
        conn.close()

        # 5. 성공 시 페이지 리다이렉트
        return redirect(url_for("browse"))  # browse 페이지로 이동

    # GET 요청일 경우 아이디어 제출 페이지 렌더링
    conn.close()
    return render_template("idea.html")

# get the texts from the Problem and Concept input boxes to generate workflow by GPT
@app.route("/generate_workflow", methods=["POST"])
@login_required
def generate_workflow():
    # 1. Get the inputed texts from client(js form)
    problem = request.form.get("problem", "")
    concept = request.form.get("concept", "")

    # 2. Create a prompt to send GPT
    prompt = f"""
    You are a Project Manager who is planning how to develop a system for a software project.

    Problem to Solve: {problem}
    Concept of the System: {concept}

    Based on the context above, please explain me how to make this software system in 6 steps. Your answer has to be maximum 700 words and, should not repeat what concept and problem stated.
    """

    # 3. Call OpenAI API (Chat completion)
    result = generator(prompt, max_length=800, do_sample=True)
    workflow = result[0]["generated_text"]

    # 4. Return result
    return jsonify({"workflow": workflow[:800]})

@app.route("/detail/<int:idea_id>")
@login_required
def detail(idea_id):
    conn = get_db()
    cur = conn.cursor()

    # 1. Get specific ID
    cur.execute("SELECT ideas.*, users.username FROM ideas JOIN users ON ideas.user_id = users.id WHERE ideas.id = ?", (idea_id,))
    idea = cur.fetchone()

    conn.close()

    # 2. If no exist, show 404 error
    if not idea:
        return render_template("apology.html", message="Idea not found")

    # 3. Check whether the login user is the owner of the idea
    if idea["user_id"] == session["user_id"]:
        user_role = "Owner"
    else: 
        user_role = "Watcher"

    # 4. Swtich team_members to a list which were saved seperately by comma 
    team_members = idea["team_members"].split(".")

    return render_template("detail.html", idea=idea, user_role=user_role, team_members=team_members)


@app.route("/browse", methods=["GET", "POST"])
def browse():
    conn = get_db()
    cur = conn.cursor()

    # Get all the data from the ideas table
    cur.execute("SELECT * FROM ideas ORDER BY created_at DESC")
    ideas = cur.fetchall()

    # count project numbers
    project_count = len(ideas)

    return render_template("browse.html", ideas=ideas, project_count=project_count)

@app.route("/apology")
def show_apology():
    return render_template("apology.html", top=400, bottom="Something went wrong")

if __name__ == "__main__":
    app.run(debug=True)
