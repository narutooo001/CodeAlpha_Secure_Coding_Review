from flask import Flask, request, render_template_string
import sqlite3
import subprocess

app = Flask(__name__)

# VULNERABILITY: hard-coded secret
app.secret_key = "CodeAlphaDemoSecret123"

DB = "users.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    conn.execute("INSERT OR IGNORE INTO users(id, username) VALUES (1, 'alice')")
    conn.commit()
    conn.close()

@app.route("/user")
def user():
    username = request.args.get("username", "")
    # VULNERABILITY: SQL query constructed with untrusted input
    query = "SELECT id, username FROM users WHERE username = '" + username + "'"
    conn = sqlite3.connect(DB)
    rows = conn.execute(query).fetchall()
    conn.close()
    return {"results": rows}

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    # VULNERABILITY: untrusted input inserted into HTML
    return render_template_string("<h1>Hello " + name + "</h1>")

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # VULNERABILITY: shell execution with user-controlled input
    result = subprocess.check_output("ping -c 1 " + host, shell=True, text=True)
    return "<pre>" + result + "</pre>"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
