import hashlib
import time

def generate_token(username):
	salted = username+str(time.time())
	token = hashlib.sha256(salted.encode()).hexdigest()
	print(token)
	return token

def hash_sha256(string:str):
	return hashlib.sha256(string.encode()).hexdigest()

class Auth:
	def __init__(self, db):
		self.authenticated = []
		self.db = db
		pass
	def authenticate(self, username, password):
		print(f"Authenticating user {username} with password {password}")
		user = self.db.fetch("user",f"name='{username}'")[0]
		if user["name"] == username and user["passwd_sha256"] == hash_sha256(password):
			token = generate_token(username)
			self.authenticated.append({'user': username, 'token': token})
			user_dict = {
				'username': user["name"],
				'role': user["role"],
				'status': True,
				'token': token,
				'user_id': user["id"],
			}
		else:
			user_dict = {
				'username': username,
				'role': "unknown",
				'status': False,
				'token': "unauthenticated",
				'user_id': 0,
			}
		self.authenticated.append(user_dict)
		return user_dict

	def is_authenticated(self, username,token):
		for user in self.authenticated:
			if user['token'] == token and user['user'] == username:
				print(f"User accepted {user['user']==username}")
				print(f"Token accepted {user['token']==token}")
				return True
		return False

	def get_user(self, username):
		for user in self.authenticated:
			if user['user'] == username:
				return user

	def add_user(self, username, password, role):
		print(f"Adding user {username} with password {password} and role {role}")
		passwd = hash_sha256(password)
		user = {
			"name": username,
			"passwd_sha256": passwd,
			"role": role,
		}
		self.db.commit("user", user)



