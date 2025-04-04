class MessageClient():
	def __init__(self,db):
		self.db = db
	def get_messages(self, user):
		return self.cursor().execute("SELECT * FROM messages").fetchall()

