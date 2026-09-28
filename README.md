# CodeAlpha Task 3 — Secure Coding Review

## Project
A small Flask web application was created in two versions:
- `vulnerable_app.py` — intentionally insecure code for security review and demonstration.
- `secure_app.py` — remediated version showing safer coding practices.

## Vulnerabilities reviewed
1. SQL Injection risk from string-built SQL queries.
2. Cross-Site Scripting (XSS) risk from unsafe HTML rendering.
3. Command Injection risk from passing user input to a shell command.
4. Hard-coded application secret.
5. Weak authentication design.

## Tools / methods
- Manual source-code inspection
- Pattern-based static review
- Local execution for functional verification
- Remediation comparison

## Run locally
Create a virtual environment if desired, then install:

```bash
pip install -r requirements.txt
```

Run the secure version:

```bash
python secure_app.py
```

Open `http://127.0.0.1:5000/`.

> This project is for authorized local security education and secure-coding practice.
