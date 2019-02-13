from flask import Flask, render_template
app = Flask(__name__)

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
 }
]


@app.route("/")
def home():
    return render_template('home.html',detail = details)

if __name__ == "__main__":
    app.run(debug = True)