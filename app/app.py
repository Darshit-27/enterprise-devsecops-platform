from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "DevSecOps App Running 🚀🔥"

@app.route('/login')
def login():
    username = request.args.get('username')
    return f"Welcome {username}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
