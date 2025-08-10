from discord.ext import commands
import discord
import random
import yaml
from dotenv import load_dotenv
import os
import asyncpg
import psycopg2
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# with open('artifacts.yaml', 'r', encoding='utf-8') as f:
# 	items = yaml.safe_load(f)


def is_table_empty(tableName: str):
	response = supabase.from_(tableName).select("*").limit(1).execute()
	data = response.data

	if data:
		return False
	else:
		return True

response = (supabase.table("users").select("*").execute())
print(response)