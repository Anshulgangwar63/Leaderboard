from user import User
from Env import Env_Vars
from fetch_from_sheet import SheetData
from pymongo import MongoClient
from pprint import pprint

env_vars = Env_Vars()

MongoURI = env_vars.MongoURI
client = MongoClient(MongoURI, 27017)
db = client['users']

users = db['users']

def do_update():
  sheet = SheetData()
  data = sheet.get_sheet()
  new_uses = []
  user_scores = {}

  for user in data:
    user_scores[user['handle']] = int(user['score'])
    #If a user with this handle does not exist
    if users.find({'handle': user['handle']}).count() == 0:
      new_uses.append(User([user['name'], user['UID'], user['handle'], 0, 0]).__repr__())

  # Insert the new users into the DB    
  for user in new_uses:
    users.insert_one(user)

  # update the records
  find = users.find()
  for user in find:
    user['contests'] += 1
    x = 0
    try:
      x = user_scores[user['handle']]
    except KeyError:
      continue
    user['score'] += x
    users.save(user)


if __name__ == "__main__":
  do_update()