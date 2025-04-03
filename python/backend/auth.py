import hashlib
import time
from db import Database

def generate_token(username):
	salted = username+str(time.time())
	token = hashlib.sha256(salted.encode()).hexdigest()
	print(token)
	return token

def hash_sha256(string:str):
	return hashlib.sha256(string.encode()).hexdigest()

class Auth:
	def __init__(self):
		self.authenticated = []
		self.db = Database()
		pass
	def authenticate(self, username, password):
		print(f"Authenticating user {username} with password {password}")
		user = self.db.fetch("user",f"name=''{username}")
		if user["name"] == username and user["passwd_sha256"] == hash_sha256(password):
			token = generate_token(username)
			self.authenticated.append({'user': username, 'token': token})
			return {
				'username': user["name"],
				'role': user["role"],
				'status': True,
				'token': token
			}
		else:
			return {
				'username': username,
				'role': "unknown",
				'status': False,
				'token': "unauthenticated"
			}

	def is_authenticated(self, username,token):
		for user in self.authenticated:
			if user['token'] == token and user['user'] == username:
				print(f"User accepted {user['user']==username}")
				print(f"Token accepted {user['token']==token}")
				return True
		return False

	def add_user(self, username, password, role):
		print(f"Adding user {username} with password {password} and role {role}")
		passwd = hash_sha256(password)
		user = {
			"name": username,
			"passwd_sha256": password,
			"role": role,
		}
		self.db.commit("user", user)



