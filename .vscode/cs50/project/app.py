from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology
import sqlite3

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

def get_db():
    conn = sqlite3.connect("project.db")
    conn.row_factory = sqlite3.Row  
    return conn


@app.route("/")
def index():
    return render_template("index.html")

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
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("account"))  
        else:
            return render_template("login.html", message="Invalid username or password")
    return render_template("login.html")

@app.route("/register", method=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if not username:
            return render_template("apology.html", message="Username is required")
        if not password:
            return render_template("apology.html", message="Password is required")
        if password != confirm:
            return render_template("apology.html", message="Password do not match")

    db.execute("SELECT * FROM users WHERE = ?", (username,))
    existing_user = db.fetchone()
    if existing_user:
        return render_template("apology.html", message="Username already taken")
    
    hashed_pw = generate_password_hash(password)
    db.execute("INSERT INTO users (username, password) VALUE (?, ?)"), (username, hashed_pw)
    conn.commit()

    db.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = db.fetchone()
    session["user_id"] = user[0]

    return redirect("/account")

return render_template("registration.html")


@app.route("/idea")
@login_required
def idea():
    return render_template("apology.html")

@app.route("/projects")
@login_required
def projects():
    return render_template("apology.html")

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    if request.method == "POST":
        return apology("POST is undergoing", 200)
    return render_template("account.html")


@app.route("/apology")
def show_apology():
    return render_template("apology.html", top=400, bottom="Something went wrong")


if __name__ == "__main__":
    app.run(debug=True)
