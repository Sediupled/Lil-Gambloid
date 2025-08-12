from TableOps import is_table_empty
from user import User
from DatabaseServices import get_user_id,get_usernames_all_users,get_user,add_new_user
from InventoryServices import getInventory_db

def getUserId_db(username: str):
	user_id_response = get_user_id(username)
	return int(response.data[0]["id"])

def getUsernames():
	usernames_response = get_usernames_all_users()
	usernames = [item["username"] for item in usernames_response.data]
	return usernames

def getUser_db(username: str):
	user_response = get_user(username)

	for person in user_response.data:
		username = person['username']
		inventory = getInventory_db(username)
	return User(username, inventory)

# adds user to table and returns user object
def createUser(username: str):
	if is_table_empty("users"):
		nextId = 1
	else:
		add_new_user(username)

	return User(username)
	print(nextId)