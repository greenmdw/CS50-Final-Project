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

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html")


@app.route("/idea")
@login_required
def idea():
    return render_template("apology.html")


@app.route("/projects")
@login_required
def projects():
    return render_template("apology.html")


@app.route("/apology")
def show_apology():
    return render_template("apology.html", top=400, bottom="Something went wrong")

if __name__ == "__main__":
    app.run(debug=True)
