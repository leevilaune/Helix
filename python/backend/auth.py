
class Auth:
	def __init__(self):

		pass

	def authenticate(self, username, password):
		print(f"Authenticating user {username} with password {password}")
		if username == 'user' and password == 'pwd':
			return {
				'username': username,
				'role': "user",
				'status': True
			}
		elif username == 'admin' and password == 'admin':
			return  {
				'username': username,
				'role': "admin",
				'status': True
			}
		else:
			return {
				'username': username,
				'role': "unknown",
				'status': False,
			}