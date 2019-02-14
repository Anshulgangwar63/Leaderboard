from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
import sys
sys.path.insert(0, './db/')

app = Flask(__name__)
from Env import Env_Vars
env_vars = Env_Vars()

MongoURI = env_vars.MongoURI
client = MongoClient(MongoURI, 27017)
db = client['users']

users = db['users']

details = [
    {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
     "Rank":3,
    "name":"Abhishek",
    "UID":"17bcs1612",
    "handle":"abhiy13",
    "score":2000
 },
 {
     
     "Rank":2,
    "name":"Manvendra",
    "UID":"17bcs1614",
    "handle":"ms_007",
    "score":3000
 },
 {   
     "Rank":1,
    "name":"Yash",
    "UID":"17bcs1613",
    "handle":"yash9950",
    "score":4000
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 },
 {
    "Rank":4,
    "name":"Anshul",
    "UID":"17bcs1604",
    "handle":"anshul1999",
    "score":1064
 }
]

@app.route("/home")
@app.route("/")
def home():
   wtf = []
   rank = 1
   people = users.find().sort('score', -1)
   for p in people:
      wtf.append({
         "Rank": rank,
         "name": p['name'],
         "UID": p['UID'] ,
         "handle": p['handle'],
         "score": p['score']
      })
      rank += 1
   return render_template('home.html',detail = wtf)

@app.route("/update")
def update():
   import update as ud
   ud.do_update()
   return redirect(url_for('home'))

if __name__ == "__main__":
   app.run(debug = True)