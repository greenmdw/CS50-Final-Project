from flask import Flask, request, render_template, session, redirect, url_for, jsonify, flash
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


@app.route("/account")
@login_required
def account():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    # User data
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    if not user:
        conn.close()
        return apology("User not found", 400)

    # Owner ideas
    cur.execute("""
        SELECT ideas.*, 'Owner' AS role
        FROM ideas
        WHERE user_id = ?
    """, (user_id,))
    owner_ideas = cur.fetchall()

    # Participant ideas
    cur.execute("""
        SELECT ideas.*, participants.role AS role
        FROM ideas
        JOIN participants ON ideas.id = participants.project_id
        WHERE participants.user_id = ? AND ideas.user_id != ?
    """, (user_id, user_id))
    participant_ideas = cur.fetchall()

    # bring together
    all_ideas = owner_ideas + participant_ideas
    project_count = len(all_ideas)

    conn.close()

    return render_template(
        "account.html",
        user=user,
        ideas=all_ideas,
        project_count=project_count,
    )

@app.route("/leave_idea/<int:idea_id>", methods=["POST"])
@login_required
def leave_idea(idea_id):
    user_id = session["user_id"]

    conn = get_db()
    cur = conn.cursor()

    # Delete my data from participants table 
    cur.execute("DELETE FROM participants WHERE project_id = ? AND user_id = ?", (idea_id, user_id))
    conn.commit()
    conn.close()

    flash("You have left the project.", "success")
    return redirect(url_for("account"))

@app.route("/delete_idea/<int:idea_id>", methods=["POST"])
@login_required
def delete_idea(idea_id):
    user_id = session.get("user_id")

    conn = get_db()
    cur = conn.cursor()

    # Check I can only delete my own ideas
    cur.execute("SELECT * FROM ideas WHERE id = ? AND user_id = ?", (idea_id, user_id))
    idea = cur.fetchone()
    if not idea:
        conn.close()
        return apology("You don't have permission to delete this project.", 403)

    # Delete project(idea)
    cur.execute("DELETE FROM ideas WHERE id = ? AND user_id = ?", (idea_id, user_id))
    conn.commit()
    conn.close()

    # Flash success message
    flash("Project Deleted successfully.", "success")

    # Redirect to account.html
    return redirect(url_for("account"))


@app.route("/idea", methods=["GET", "POST"])
@login_required
def idea():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        # 1. Bring form data
        title = request.form.get("title")
        problem = request.form.get("problem")
        concept = request.form.get("concept")
        workflow = request.form.get("workflow")  # optional
        team_members = request.form.getlist("team_members")  # multiple check boxes
        project_style = request.form.get("project_style")

        # 2. authenticattion
        if not title or not problem or not concept or not team_members or not project_style:
            conn.close()
            return render_template("idea.html", message="Please fill in all required fields")

        # 3. Collect team_members value by ,
        team_members_str = ",".join(team_members)

        # 4. Insert DB
        cur.execute(
            "INSERT INTO ideas (user_id, title, problem, concept, workflow, team_members, project_style) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (session["user_id"], title, problem, concept, workflow, team_members_str, project_style)
        )
        conn.commit()
        conn.close()

        # 5. If success, redirect to the page 
        return redirect(url_for("browse"))  

    # If it's a GET request, render idea.html
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

@app.route("/detail/<int:idea_id>", methods=["GET"])
@login_required
def detail(idea_id):
    user_id = session["user_id"]

    conn = get_db()
    cur = conn.cursor()

    # 1. Bring idea info
    cur.execute("""
        SELECT ideas.*, users.username 
        FROM ideas 
        JOIN users ON ideas.user_id = users.id 
        WHERE ideas.id = ?
    """, (idea_id,))
    idea = cur.fetchone()
    if not idea:
        conn.close()
        return render_template("apology.html", message="Idea not found")

    # 2. Convert team_members to list
    team_members = [m.strip() for m in idea["team_members"].split(",")]

    # 3. Get all participants for this idea
    cur.execute("""
        SELECT role, user_id
        FROM participants
        WHERE project_id = ?
    """, (idea_id,))
    participants = cur.fetchall()

    # 4. Determine team_status (role: username or None)
    team_status = {}
    for role in team_members:
        # If there is a participate in the same username, if there is no, show None
        joined = next((p["user_id"] for p in participants if p["role"] == role), None)
        if joined:
            # Change user_id to username 
            cur.execute("SELECT username FROM users WHERE id = ?", (joined,))
            team_status[role] = cur.fetchone()["username"]
        else:
            team_status[role] = None

    # 5. Determine current user's role
    user_participation = next((p for p in participants if p["user_id"] == user_id), None)
    if idea["user_id"] == user_id:
        user_role = "Owner"
    elif user_participation:
        user_role = user_participation["role"]
    else:
        user_role = None

    conn.close()

    return render_template(
        "detail.html",
        idea=idea,
        user_role=user_role,
        team_members=team_members,
        team_status=team_status
    )


@app.route("/join_idea/<int:idea_id>", methods=["POST"])
@login_required
def join_idea(idea_id):
    role = request.form.get("role")
    user_id = session["user_id"]

    if not role:
        return redirect(url_for("detail", idea_id=idea_id))

    conn = get_db()
    cur = conn.cursor()

    # check whether already participated role
    cur.execute("""
        SELECT * FROM participants WHERE project_id = ? AND role = ?
    """, (idea_id, role))
    if cur.fetchone():
        conn.close()
        return render_template("apology.html", message="This role has already been joined.")

    # check whether the user already joined this idea
    cur.execute("""
        SELECT * FROM participants WHERE project_id = ? AND user_id = ?
    """, (idea_id, user_id))
    if cur.fetchone():
        conn.close()
        return render_template("apology.html", message="You have already joined this project.")

    # Register Join
    cur.execute("""
        INSERT INTO participants (project_id, user_id, role)
        VALUES (?, ?, ?)
    """, (idea_id, user_id, role))
    conn.commit()
    conn.close()

    return redirect(url_for("detail", idea_id=idea_id))


@app.route("/browse", methods=["GET", "POST"])
def browse():
    conn = get_db()
    cur = conn.cursor()

    # bring data of ideas and writers, and each idea's participants
    cur.execute("""
        SELECT i.*,
               (SELECT COUNT(*) FROM participants p WHERE p.project_id = i.id) AS joined_count,
               u.username AS writer
        FROM ideas i
        JOIN users u ON i.user_id = u.id
        ORDER BY i.created_at DESC
    """)
    ideas = cur.fetchall()

    # Total project numbers
    project_count = len(ideas)

    conn.close()
    return render_template("browse.html", ideas=ideas, project_count=project_count)


@app.route("/apology")
def show_apology():
    return render_template("apology.html", top=400, bottom="Something went wrong")

if __name__ == "__main__":
    app.run(debug=True)
