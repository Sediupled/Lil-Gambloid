from supabase import create_client, Client
from dotenv import load_dotenv
import os
from item import *

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#User DB OPS

def get_user_id(username: str):
	response = (
		supabase.table("users")
		.select("id")
		.eq("username", username)
		.execute()
	)

	return response

def get_usernames_all_users():
	response = (
		supabase.table("users")
		.select("username")
		.execute()
	)
	return response

def get_user(username: str):
	response = (
		supabase.table("users")
		.select("*")
		.eq("username", username)
		.execute()
	)
	return response

# adds user to table and returns user object
def add_new_user(username: str):
	response = (
		supabase.table("users")
		.select("id")
		.order("id", desc=True)
		.limit(1)
		.execute()
	)
	nextId = response.data[0]["id"] + 1

	response = (
		supabase.table("users")
		.insert({"id": nextId,"username": username})
		.execute()
	)

#Item DB OPS

# gets Item from db by name and returns an Item obj
def get_item_from_db(name: str):
	response = (
		supabase.table("items")
		.select("*")
		.eq("name", name)
		.execute()	
	)
	return response

# Gets All Item from DB
def get_all_items():
	response = (
		supabase.table("items")
		.select("*")
		.execute()	
	)

	return response
# Inventory DB OPS

def getInvenData(username: str):
	response = (
		supabase.table("users")
		.select("username, inventory(item_name,quantity)")
		.eq("username", username)
		.execute()
	)

	return response

def increment_item_quantity(username, item):
	ID_response = get_user_id(username)
	ID = int(ID_response.data[0]["id"])

	response1 = (
		supabase.table("inventory")
		.select("quantity")
		.eq("item_name", item.getName())
		.eq("user_id", ID)
		.execute()
	)
	quantityVal = int(response1.data[0]["quantity"])

	response2 = (
	supabase.table("inventory")
	.update({"quantity": quantityVal + 1})
	.eq("item_name", item.getName())
	.eq("user_id", ID)
	.execute()
	)

	print(response2.data)

def add_new_item(username, item):
	ID_response = get_user_id(username)
	ID = int(ID_response.data[0]["id"])
	response = (
			supabase.table("inventory")
			.insert({"user_id": ID, "quantity": 1, "item_name": item.getName()})
			.execute()
		)