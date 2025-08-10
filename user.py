from dataclasses import dataclass
@dataclass
class User:
	name: str
	inventory : list

	def __init__(self, name, inventory = []):
		self.name = name
		self.inventory = inventory

	def getName(self):
		return self.name

	def getInventory(self):
		return self.inventory