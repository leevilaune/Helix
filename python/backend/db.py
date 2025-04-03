import mysql.connector
import os

class Database:
	def __init__(self):
		self.connection = mysql.connector.connect(
			host="127.0.0.1",
			port=3306,
			database="helixdb",
			user=os.getenv("DB_USER"),
			password=os.getenv("DB_PASSWORD"),
			autocommit=True
		)
		self.cursor = self.connection.cursor(dictionary=True)

	def commit(self, table, data):
		try:
			columns = ", ".join(f"`{key}`" for key in data.keys())
			placeholders = ", ".join(["%s"] * len(data))
			values = tuple(data.values())

			query = f"INSERT INTO `{table}` ({columns}) VALUES ({placeholders})"
			self.cursor.execute(query, values)
			return True
		except Exception as e:
			print(e)
			return False

	def fetch(self,table:str, condition:str):
		try:
			query = f"SELECT * FROM `{table}` WHERE `{condition}`"
			self.cursor.execute(query)
			return self.cursor.fetchall()
		except Exception as e:
			print(e)
			return None

	def update(self):
		pass


	def delete(self):
		pass

	def execute(self, query):
		try:
			self.cursor.execute(query)
			return True
		except Exception as e:
			print(e)
			return False