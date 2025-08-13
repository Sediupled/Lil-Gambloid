from dataclasses import dataclass
@dataclass
class Item:
	
	name: str
	emoji: str
	amount: int
	rarity: int
	description: str

	def __init__(self, name, emoji,amount, rarity, description):
		self.name = name
		self.emoji = emoji
		self.amount = amount
		self.rarity = rarity
		self.description = description

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

	def getRarity(self):
		return self.rarity

	def getDescription(self):
		return self.description