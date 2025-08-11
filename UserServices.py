from supabase import create_client, Client 
from dotenv import load_dotenv
import os
# from TableOps import *
from user import *
from InventoryServices import getInventory_db

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def getUser_db(username: str):
	response = (
		supabase.table("users")
		.select("*")
		.eq("username", username)
		.execute()
	)

	for person in response.data:
		username = person['username']
		inventory = getInventory_db(username)
	return User(username, inventory)

def getUsernames():
	response = (
		supabase.table("users")
		.select("username")
		.execute()
	)
	usernames = [item["username"] for item in response.data]
	return usernames

# adds user to table and returns user object
def createUser(username: str):
	if is_table_empty("users"):
		nextId = 1
	else:
		print("table is not empty")
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

	return User(username)
	print(nextId)


# finds user by name and updates it to the new name
def updateUsername(username: str):
	response = (
		supabase.table("users")
		.update({"username": username})
		.eq("username", self.name)
		.execute()
	)
	print(f"Old Name: {self.name} -> New Name: {username}")

def getUserId_db(username: str):
	response = (
		supabase.table("users")
		.select("id")
		.eq("username", username)
		.execute()
	)
	return int(response.data[0]["id"])

# getUser("properchai")

# createUser("test_user_1")