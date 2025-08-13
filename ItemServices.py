from item import Item
from DatabaseServices import get_item_from_db, get_all_items, get_rarity_wise_item
import random

# gets Item from db by name and returns an Item obj
def getItem_db(name: str, amount: int):
	item_response = get_item_from_db(name)
	item = item_response.data[0]
	return Item(item["name"], item["emoji"], amount, item["rarity"], item["description"])

# Gets All Item from DB
def getAllItems_db():
	ItemList = []

	all_items_response = get_all_items()
	
	for item in all_items_response.data:
		item =  Item(item["name"], item["emoji"], 1, item["rarity"], item["description"])
		ItemList.append(item)

	return ItemList

def getItemByRarity():
	# pdb.set_trace()
	rarities_dict = {
	"Common": 70,
	"Uncommon": 20,
	"Rare": 5,
	"Epic": 3,
	"Legendary" : 2
	}

	rolled_num = random.randint(1,100)
	print(rolled_num)
	total_prob = 0

	for rarity, prob in rarities_dict.items():
		total_prob += prob
		if rolled_num <= total_prob:
			response_item = get_rarity_wise_item(rarity)
			break

	item_got = random.choice(response_item.data)

	item =  Item(item_got["name"], item_got["emoji"], 1, item_got["rarity"], item_got["description"])

	return item