from flask import Flask, request, jsonify, render_template
import sqlite3
import subprocess
import os

app = Flask(__name__)

# REMEDIATION: load secret from environment instead of hard-coding it
app.secret_key = os.environ.get("APP_SECRET", "local-development-only")

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
    # REMEDIATION: parameterized query
    query = "SELECT id, username FROM users WHERE username = ?"
    conn = sqlite3.connect(DB)
    rows = conn.execute(query, (username,)).fetchall()
    conn.close()
    return jsonify({"results": rows})

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    # REMEDIATION: template engine escapes HTML by default
    return render_template("hello.html", name=name)

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # REMEDIATION: allow-list basic hostname/IP characters and avoid shell=True
    import re
    if not re.fullmatch(r"[A-Za-z0-9.:-]{1,253}", host):
        return jsonify({"error": "Invalid host"}), 400
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True,
        check=False
    )
    return "<pre>" + result.stdout + "</pre>"

@app.route("/")
def index():
    return jsonify({
        "project": "CodeAlpha Secure Coding Review",
        "status": "secure-demo"
    })

if __name__ == "__main__":
    init_db()
    app.run(debug=False)
