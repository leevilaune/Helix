class MessageClient():
	def __init__(self,db):
		self.db = db
	def get_messages(self, user_id):
		return self.db.fetch("messages",f"sender={user_id}")

