from supabase import create_client, Client 
from dotenv import load_dotenv
import os
from user import *
from ItemServices import *
from item import *

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def getInventory_db(username: str):
	response = (
		supabase.table("users")
		.select("username, inventory(item_name,quantity)")
		.eq("username", username)
		.execute()
	)
	inven_list = []
	for person in response.data:
		inventory = person['inventory']
		for item in inventory:
			inven_list.append(getItem_db(str(item["item_name"]),int(item["quantity"])))
	return inven_list

#Checks if item in db, if yes just increment quantity else add item fully
def addItem_db(username, item):
	from UserServices import getUserId_db
	ID = getUserId_db(username)
	if(isIteminInven(username, item)):
		response1 = (
			supabase.table("inventory")
			.select("quantity")
			.eq("item_name", item.getName())
			.eq("user_id", ID)
			.execute()
		)
		quantityVal = int(response1.data[0]["quantity"])
		print(quantityVal)
		print(response1.data)

		response2 = (
		supabase.table("inventory")
		.update({"quantity": quantityVal + 1})
		.eq("item_name", item.getName())
		.eq("user_id", ID)
		.execute()
		)

		print(response2.data)
	else:
		response = (
			supabase.table("inventory")
			.insert({"user_id": ID, "quantity": 1, "item_name": item.getName()})
			.execute()
		)
		print(response.data)
	print("Item added")


#Helper checks if item in userinven
def isIteminInven(username, item):
	inventory_list = getInventory_db(username)
	for i in inventory_list:
		if item.getName() == i.getName():
			print("Item is already in inven")
			return True
	print("Item is NOT in inven")
	return False
