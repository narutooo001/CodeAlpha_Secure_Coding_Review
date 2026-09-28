# CodeAlpha Task 3 — Secure Coding Review Report

## 1. Objective
Review a small Python Flask application, identify common security weaknesses through manual/static inspection, and document practical remediations.

## 2. Application
Python Flask demo application with user lookup, greeting, and ping functionality.

## 3. Findings
### SC-01 — SQL Injection
**Problem:** The vulnerable version builds SQL using string concatenation.

**Fix:** Parameterized SQL query:
`SELECT id, username FROM users WHERE username = ?`

### SC-02 — Cross-Site Scripting
**Problem:** Request data is directly inserted into HTML.

**Fix:** Render through a template and rely on automatic HTML escaping.

### SC-03 — Command Injection
**Problem:** User input is passed to a shell command with `shell=True`.

**Fix:** Use `subprocess.run()` with an argument list, avoid shell execution, and validate input.

### SC-04 — Hard-coded Secret
**Problem:** The application secret is stored in source code.

**Fix:** Read it from an environment variable or a managed secret store.

### SC-05 — Debug Mode
**Problem:** Debug mode is enabled in the vulnerable version.

**Fix:** Disable debug mode for deployed applications.

## 4. Secure Coding Recommendations
- Treat all external input as untrusted.
- Prefer parameterized database queries.
- Use framework-provided output encoding.
- Avoid shell commands when a library/API can perform the operation.
- Never commit real credentials or secrets.
- Disable debug/development settings in production.
- Perform code review and automated security checks before deployment.

## 5. Conclusion
The review demonstrates how common coding patterns can introduce security weaknesses and how small implementation changes can reduce those risks. The project contains both vulnerable examples for analysis and a remediated implementation for comparison.
