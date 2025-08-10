from supabase import create_client, Client 
from dotenv import load_dotenv
import os
from TableOps import *
from user import *

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def getItem_db(name: str, amount: int):
	print("Yahan tak sorted")
	response = (
		supabase.table("items")
		.select(*)
		.eq("name", name)
		.execute()	
	)

	item = response.data

	return Item(item["name"], item["emoji"], amount)
