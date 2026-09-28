# Secure Coding Review

## Scope
Manual and static review of `vulnerable_app.py`, followed by comparison with `secure_app.py`.

| ID | Finding | Evidence | Risk | Remediation |
|---|---|---|---|---|
| SC-01 | SQL Injection | User input is concatenated into a SQL statement | High | Use parameterized queries / prepared statements |
| SC-02 | XSS | User input is directly inserted into an HTML string | High | Use a template engine with output escaping and validate input |
| SC-03 | Command Injection | User input reaches a shell command with `shell=True` | Critical | Avoid shell execution; pass arguments as a list and validate input |
| SC-04 | Hard-coded secret | Secret is embedded directly in source code | Medium | Load secrets from environment variables or a secret manager |
| SC-05 | Debug mode enabled | `app.run(debug=True)` in the vulnerable version | Medium | Disable debug mode outside development |

## Methodology
1. Identify external input sources.
2. Trace input to sensitive operations.
3. Record the security impact.
4. Apply a safer coding pattern.
5. Compare vulnerable and remediated implementations.

## Verification
The secure version:
- uses SQL parameters;
- uses Jinja template escaping;
- avoids `shell=True`;
- validates the host input;
- loads the secret from an environment variable;
- disables Flask debug mode.

No real external target or unauthorized system is involved.
