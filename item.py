from dataclasses import dataclass
@dataclass
class Item:
	
	name: str
	emoji: str
	amount: int

	def __init__(self, name, emoji,amount = 0):
		self.name = name
		self.emoji = emoji
		self.amount = amount

	def increment_item(self):
		self.amount+=1

	def change_name(self, new_name):
		self.name = new_name
		

	def getItem(self):
		return self

	def getName(self):
		return self.name

	def getAmount(self):
		return self.amount

	def getEmoji(self):
		return self.emoji