import os
from flask import Flask, request, jsonify,render_template
from backend.auth import Auth

app = Flask(__name__)
auth_client = Auth()
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/user/<user>", methods=['GET'])
def user(user: str):
    token = request.args.get("token")
    print(token, auth_client.is_authenticated(user, token))
    if(auth_client.is_authenticated(user, token)):
        return render_template("user.html",user=user, auth_status="fully authenticated")
    else:
        return render_template("user.html",user=user, auth_status="not authenticated")

@app.route("/auth", methods=["POST","GET"])
def auth():
    data = request.get_json()["data"]
    print(data)
    if not data:
        return jsonify({"error": "Invalid or no JSON data received"}), 400

    username = data.get('name')
    password = data.get('password')
    return jsonify(auth_client.authenticate(username, password))

@app.route("/auth/check",methods=["POST","GET"])
def auth_check():
    data = request.get_json()["data"]
    if(not data):
        return jsonify({"error": "Invalid or no JSON data received"}), 400
    token = data.get('token')
    user = data.get('name')
    return jsonify(auth_client.is_authenticated(user, token))
app.run(debug=True, host='0.0.0.0', port=80)