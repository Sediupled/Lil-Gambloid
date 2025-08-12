from ItemServices import getItem_db
from DatabaseServices import getInvenData, increment_item_quantity, add_new_item
from item import *
# import pdb

def getInventory_db(username: str):
	inventory_response = getInvenData(username)
	inven_list = []
	for person in inventory_response.data:
		inventory = person['inventory']
		for item in inventory:
			inven_list.append(getItem_db(str(item["item_name"]),int(item["quantity"])))
	return inven_list

#Helper checks if item in userinven
def isIteminInven(username, item):
	inventory_list = getInventory_db(username)
	return any(item.getName() == i.getName() for i in inventory_list)


#Checks if item in db, if yes just increment quantity else add item fully
def addItem_db(username, item):
	# pdb.set_trace()
	print(type(item))
	print("Running add Condition")
	if isIteminInven(username, item):
		increment_item_quantity(username, item)
	else:
		print("Adding Freshly")
		add_new_item(username,item)
	print("Item added")