from supabase import create_client, Client 
from dotenv import load_dotenv
import os
from TableOps import *
from user import *
from item import *

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# gets Item from db by name and returns an Item obj
def getItem_db(name: str, amount: int):
	response = (
		supabase.table("items")
		.select("*")
		.eq("name", name)
		.execute()	
	)

	item = response.data[0]
	return Item(item["name"], item["emoji"], amount)

# Gets All Item from DB
def getAllItems_db():
	ItemList = []

	response = (
		supabase.table("items")
		.select("*")
		.execute()	
	)
	for item in response.data:
		item =  Item(item["name"], item["emoji"], 1)
		ItemList.append(item)

	return ItemList
