from discord.ext import commands
import discord
import random
from dotenv import load_dotenv
import os
from supabase import create_client, Client
from item import Item
from user import User
from UserServices import getUsernames, getUser_db, createUser
from InventoryServices import addItem_db
from ItemServices import getAllItems_db,  getItemByRarity
# import pdb


load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


BOT_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1398566565200265268

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

# Get items from db and then pick one at random, get name and emoji, add it to inventory in db
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user) 
async def fish(ctx):
	# pdb.set_trace()
	item = getItemByRarity()

	
	addItem_db(ctx.author.name,item)

	print(f"{item.getName()}: {item.getEmoji()}")
	msg = f"You fished up: {item.getName()} {item.getEmoji()} \n"
	msg += f" Rarity: {item.getRarity()} \n"
	msg += f" This shi say: {item.getDescription()}"

	await ctx.send(msg)

@fish.error
async def fish_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need 	to wait {error.retry_after:.1f} seconds before fishing again!")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def inven(ctx):
	# pdb.set_trace()
	user = getUser_db(ctx.author.name)
	inventory = user.getInventory()
	if not inventory:
		await ctx.send(f"Your Inventory is Empty T_T")
	else:
		msg = f"These are your items: \n"
		for item in inventory:
			msg += f"{item.getEmoji()} {item.getName()}: {item.getAmount()} \n"

		await ctx.send(msg)
@inven.error
async def inven_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need to wait {error.retry_after:.1f} seconds before checking your inventory again!")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def allitems(ctx):
	msg = "These are all the items: \n"
	item_list = getAllItems_db()

	for item in item_list:
		msg += f"{item.getEmoji()} {item.getName()} \n"
		msg += f"Rarity: {item.getRarity()} \n"
		msg += "\n"

	await ctx.send(msg)
@inven.error
async def inven_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"🕒 You need to wait {error.retry_after:.1f} seconds before checking your inventory again!")


bot.run(BOT_TOKEN)