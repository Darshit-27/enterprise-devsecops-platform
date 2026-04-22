from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

# 🔐 Security Headers (Fix ZAP Findings)
@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Permissions-Policy'] = "geolocation=()"
    response.headers['Referrer-Policy'] = "no-referrer"
    return response


# 🏠 Home Route
@app.route('/')
def home():
    return "DevSecOps App Running 🚀🔥"


# 🔐 Login Route (Safe Input Handling)
# Note: CSRF protection is not required here as this endpoint only handles GET requests
# and does not perform any state-changing operations.
@app.route('/login')
def login():
    username = request.args.get('username', '')
    return f"Welcome {escape(username)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
