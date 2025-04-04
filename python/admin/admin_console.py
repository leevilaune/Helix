from python.backend.db import Database
import python.backend.auth as auth

auth = auth.Auth()

user = input("Username: ")
password = input("Password: ")

credentials = auth.authenticate(user, password)
is_auth = auth.is_authenticated(user,credentials["token"])

if is_auth and credentials["role"] == "admin":
	while True:
		print("Admin tools")
		user_input = input("> ")
		if user_input == "exit":
			break
		elif "add_user" in user_input:
			split_str = user_input.split(" ")
			auth.add_user(split_str[1], split_str[2], split_str[3])

