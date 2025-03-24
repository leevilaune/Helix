import os
from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    backend_url = os.getenv('BACKEND_URL','http://80.220.204.247:3000')
    return render_template("index.html",backend_url=backend_url)

@app.route("/user/<user>")
def user(user: str):
    return render_template("user.html",user=user)

app.run(debug=True, host='0.0.0.0', port=80)
