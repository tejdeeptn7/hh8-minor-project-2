from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_SQL_PASSWORD",
        database="iam_rbac"
    )

def get_role(username):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT r.role_name FROM users u
        JOIN user_roles ur ON u.id = ur.user_id
        JOIN roles r ON ur.role_id = r.id
        WHERE u.username = %s
    """, (username,))
    role = cur.fetchone()
    return role[0] if role else None

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                    (username, password))
        user = cur.fetchone()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        return "Invalid credentials"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    role = get_role(session["user"])
    return render_template("dashboard.html", role=role)

@app.route("/admin")
def admin():
    if "user" not in session:
        return redirect("/")
    role = get_role(session["user"])
    if role == "admin":
        return render_template("admin.html")
    return "Access Denied ❌"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
