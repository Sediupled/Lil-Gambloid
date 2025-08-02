from dataclasses import dataclass
from inventory import Inventory

@dataclass
class User:
	name: str
	inventory: Inventory


	def __init__(self, name):
		self.name = name
		self.Inventory = Inventory()

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name 

	def getInventory(self):
		return self.inventory