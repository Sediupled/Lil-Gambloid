from item import Item
from DatabaseServices import get_item_from_db, get_all_items

# gets Item from db by name and returns an Item obj
def getItem_db(name: str, amount: int):
	item_response = get_item_from_db(name)
	item = item_response.data[0]
	return Item(item["name"], item["emoji"], amount)

# Gets All Item from DB
def getAllItems_db():
	ItemList = []

	all_items_response = get_all_items()
	
	for item in all_items_response.data:
		item =  Item(item["name"], item["emoji"], 1)
		ItemList.append(item)

	return ItemList