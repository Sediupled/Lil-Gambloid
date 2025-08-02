from discord.ext import commands
import discord
from inventory import Inventory
from item import Item
import random
import yaml
from dotenv import load_dotenv
import os
import asyncpg
import psycopg2
from supabase import create_client, Client
import json

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


BOT_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1398566565200265268

with open('artifacts.yaml', 'r', encoding='utf-8') as f:
	items = yaml.safe_load(f)

bot = commands.Bot(command_prefix=">" , intents=discord.Intents.all())

def is_table_empty(tableName: str):
	response = supabase.from_(tableName).select("*").limit(1).execute()
	data = response.data

	if data:
		return False
	else:
		return True

def getUsernames():
	response = (
		supabase.table("users")
		.select("username")
		.execute()
	)

	usernames = [item["username"] for item in response.data]
	return usernames

def user_create(username: str):

	if is_table_empty("users"):
		nextId = 1
	else:
		response = (
			supabase.table("users")
			.select("id")
			.order("id", desc=True)
			.limit(1)
			.execute()
		)
		nextId = response.data[0]["id"] + 1
		print(nextId)

	response = (
		supabase.table("users")
		.insert({"id": nextId, "username": username})
		.execute()
		)

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if str(message.author) not in getUsernames():
		user_create(message.author.name)
	else:
		print("User exists")
	await bot.process_commands(message)

@bot.event
async def on_ready():

	print(f'Bot is ready! Logged in as {bot.user}')
	print("BJ Time!!!")
	channel = bot.get_channel(CHANNEL_ID)
	await channel.send("BJ Time!!!")

@bot.command()
async def yo(ctx, arg1 = ""):
	if arg1 == "":	
		await ctx.send("Yo")
		return
	elif arg1.lower() == "boy":
		await ctx.send("Fuck off Asmi!!")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user) 
async def fish(ctx):
	item_data = random.choice(items['artifacts'])
	item = Item(item_data['name'], item_data['emoji']) 
	inventory.add_item_inven(item)
	print(f"{item_data['name']}: {item_data['emoji']}")
	await ctx.send(f"You fished up: {item_data['name']} {item_data['emoji']}")

@fish.error
async def fish_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need 	to wait {error.retry_after:.1f} seconds before fishing again!")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def inven(ctx):
	inventory_list = inventory.get_inventory()
	if not inventory_list:
		print("Your Inventory is Empty T_T")
		await ctx.send(f"Your Inventory is Empty T_T")
		return

	item_desc = []
	for i in inventory_list:
		item_desc.append((i.getName(), i.getAmount(), i.getEmoji()))
	for item in item_desc:
		print(item[2], " ", item[0],": ",item[1])
	msg = "You have these items:\n"
	for item in item_desc:
		msg += f"{item[2]} {item[0]}: {item[1]}\n"

	await ctx.send(msg)
@inven.error
async def fish_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need to wait {error.retry_after:.1f} seconds before checking your inventory again!")


bot.run(BOT_TOKEN)