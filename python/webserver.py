import os
from flask import Flask, request, jsonify,render_template
from backend.auth import Auth
from backend.db import Database
from backend.messages import MessageClient

app = Flask(__name__)
db = Database()
auth_client = Auth(db=db)
msg = MessageClient(db=db,auth=auth_client)
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/user/<user>", methods=['GET'])
def user(user: str):
    token = request.args.get("token")
    print(token, auth_client.is_authenticated(user, token))
    if auth_client.is_authenticated(user, token):
        return render_template("user.html",user=user, auth_status="fully authenticated")
    else:
        return render_template("user.html",user=user, auth_status="not authenticated")

@app.route("/user/get")
def get_user():
    username = request.args.get("user")
    db.fetch("user","id,name",f"name='{username}'")

@app.route("/chat")
def chat():
    if auth_client.is_authenticated(request.args.get("user"), request.args.get("token")):
        return render_template("chat.html", user = request.args.get("user"))
    else: return "not authenticated, fuck you"
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

@app.route("/api/message/send",methods=["POST","GET"])
def message_send():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error": "Invalid or no JSON data received"}), 400
    else:
        return jsonify({"success":"Message sent"}), 200

@app.route("/api/message/fetch")
def message_fetch():
   return "tbd"

app.run(debug=True, port=5000, host="0.0.0.0")
