import os
from flask import Flask, request, jsonify,render_template
from backend.auth import Auth

app = Flask(__name__)
auth_client = Auth()
@app.route("/")
def hello_world():
    backend_url = os.getenv('BACKEND_URL','http://80.220.204.247:3000')
    return render_template("index.html",backend_url=backend_url)

@app.route("/user/<user>")
def user(user: str):
    return render_template("user.html",user=user)


@app.route("/auth", methods=["POST","GET"])
def auth():
    data = request.get_json()["data"]
    print(data)
    if not data:
        return jsonify({"error": "Invalid or no JSON data received"}), 400

    username = data.get('name')
    password = data.get('password')
    return jsonify(auth_client.authenticate(username, password))

app.run(debug=True, host='0.0.0.0', port=80)
