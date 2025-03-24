import hashlib
import time
from tokenize import generate_tokens


class Auth:
	def __init__(self):
		self.authenticated = []
		pass
	def authenticate(self, username, password):
		print(f"Authenticating user {username} with password {password}")
		if username == 'user' and password == 'pwd':
			token = self.generate_token(username)
			self.authenticated.append({'user': username, 'token': token})
			return {
				'username': username,
				'role': "user",
				'status': True,
				'token': token
			}
		elif username == 'admin' and password == 'admin':
			token = self.generate_token(username)
			self.authenticated.append({'user': username, 'token': token})
			return  {
				'username': username,
				'role': "admin",
				'status': True,
				'token': token
			}
		else:
			return {
				'username': username,
				'role': "unknown",
				'status': False,
				'token': ""
			}

	def is_authenticated(self, username,token):
		for user in self.authenticated:
			if user['token'] == token and user['user'] == username:
				print(f"User accepted {user['user']==username}")
				print(f"Token accepted {user['token']==token}")
				return True
		return False

	def generate_token(self, username):
		salted = username+str(time.time())
		token = hashlib.sha256(salted.encode()).hexdigest()
		print(token)
		return token