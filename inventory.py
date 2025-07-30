from dataclasses import dataclass

@dataclass
class Inventory:

	item_arr: list

	def __init__(self):
		self.item_arr = []

	def add_item_inven(self, item):
		item_names = []
		inventory_temp = self.get_inventory()
		for i in inventory_temp:
			item_names.append(i.getName())

		if item.getName() not in item_names:
			self.item_arr.append(item)
			item.increment_item()
		else:
			inventory_temp = self.get_inventory()
			for i in inventory_temp:
				if item.getName() == i.getName():
					i.increment_item()

	def get_inventory(self):
		return self.item_arr