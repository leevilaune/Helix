import mysql.connector, os

class MessageClient():
	def __init__(self):
		self.connection = mysql.connector.connect(
			host="127.0.0.1",
			port=3306,
			database="afkj_db",
			user=os.getenv("DB_USER"),
			password=os.getenv("DB_PASSWORD"),
			autocommit=True
		)
		self.cursor = self.connection.cursor(dictionary=True)
	def get_messages(self):
		self.connection.cursor().execute("SELECT * FROM messages")
		pass

MessageClient().get_messages()