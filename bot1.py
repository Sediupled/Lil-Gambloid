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
import user
import TableOps
from UserServices import *

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


BOT_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1398566565200265268

# with open('artifacts.yaml', 'r', encoding='utf-8') as f:
# 	items = yaml.safe_load(f)

bot = commands.Bot(command_prefix=">" , intents=discord.Intents.all())

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.author.name not in getUsernames():
		createUser(message.author.name)
		print("user doesnt exist", message.author.name)
	await bot.process_commands(message)

@bot.event
async def on_ready():

	print(f'Bot is ready! Logged in as {bot.user}')
	print("BJ Time!!!")
	channel = bot.get_channel(CHANNEL_ID)
	await channel.send("BJ Time!!!")

# TODO: make yo reply
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
	user = getUser(ctx.author.name)
	inventory = user.getInventory()
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
	user = getUser_db(ctx.author.name)
	print(f"inven ctx name: {ctx.author.name}")
	inventory = user.getInventory()
	if not inventory:
		print("Your Inventory is Empty T_T")
		await ctx.send(f"Your Inventory is Empty T_T")
	else:
		print("there is something heehee, chal coding kar bkl")
		await ctx.send(f"there is something heehee, chal coding kar bkl")

		print("These are your items: \n")
		await ctx.send(f"These are your items: \n")
	for item in inventory:
		print(f"{item.getEmoji()} {item.getName()}: {item.getAmount()}")
		await ctx.send(f"{item.getEmoji()} {item.getName()}: {item.getAmount()}")
	# await ctx.send(msg)
@inven.error
async def inven_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need to wait {error.retry_after:.1f} seconds before checking your inventory again!")


bot.run(BOT_TOKEN)