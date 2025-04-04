class MessageClient():
	def __init__(self,db,auth):
		self.db = db
		self.auth = auth
	def get_messages(self, user_id):
		return self.db.fetch("messages","*",f"sender={user_id}")

	def add_message(self, message: dict):
		self.db.commit("messages",message)
