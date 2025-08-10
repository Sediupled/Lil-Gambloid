from supabase import create_client, Client 
from dotenv import load_dotenv
import os
from TableOps import *
from user import *
from ItemSer

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

	print(f" Get user response: {response}")
	inven_list = []
	for person in response.data:
		inventory = person['inventory']
		for item in inventory:
			print(item)
			inven_list.append(getItem_db(str(item["item_name"]),int(item["quantity"])))
			print(inven_list)
	print(inven_list)
	return inven_list