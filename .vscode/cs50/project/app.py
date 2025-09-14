from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology
import sqlite3
from functools import wraps

app = Flask(__name__)

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
            conn.close
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

        # Debugging code -----------------
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            print("DEBUG session:", dict(session))  # checking session. printing on the terminal
            return redirect(url_for("account"))
        # Debugging code ends ------------

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
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
    # 세션에서 user_id 가져오기
    user_id = session.get("user_id")
    if not user_id:
        # 세션이 없으면 /login으로 보내거나 에러 처리
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    # 현재 로그인한 사용자 정보 가져오기
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    print("DEBUG account - fetched user:", dict(user) if user else None)

    # Notifications 카운트 가져오기
    cur.execute("SELECT COUNT(*) FROM notifications WHERE user_id = ?", (user_id,))
    notifications_count = cur.fetchone()[0]
    print("DEBUG account - notifications_count:", notifications_count)

    conn.close()

    # DB에 user가 없는 경우 안전장치
    if not user:
        return apology("User not found", 400)

    # account.html에 user 정보와 notifications_count 전달
    return render_template(
        "account.html",
        user=user,
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
            "INSERT INTO projects (user_id, title, problem, concept, workflow, team_members, project_style) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (session["user_id"], title, problem, concept, workflow, team_members_str, project_style)
        )
        conn.commit()
        conn.close()

        # 5. 성공 시 페이지 리다이렉트
        return redirect(url_for("projects"))  # projects 페이지로 이동

    # GET 요청일 경우 아이디어 제출 페이지 렌더링
    conn.close()
    return render_template("idea.html")




@app.route("/projects")
@login_required
def projects():
    return render_template("apology.html")


@app.route("/apology")
def show_apology():
    return render_template("apology.html", top=400, bottom="Something went wrong")

if __name__ == "__main__":
    app.run(debug=True)
