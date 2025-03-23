from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.auth import Auth
app = Flask(__name__)
auth_client = Auth()
CORS(app)
@app.route("/auth", methods=["POST","GET"])
def auth():
	data = request.get_json()["data"]
	print(data)

	# Check if the data exists and is valid
	if not data:
		return jsonify({"error": "Invalid or no JSON data received"}), 400

	# Extract data from the JSON (example: username and password)
	username = data.get('name')
	password = data.get('password')
	return jsonify(auth_client.authenticate(username, password))

app.run(debug=True,
        port=3000,
        host='0.0.0.0')