from flask import Flask, request
from flask_pymongo import pymongo
CONNECTION_STRING = "mongodb+srv://vdssystem0:<VA123AVdkd>@cluster0.vdo3rvu.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('test')
user_collection = pymongo.collection.Collection(db, 'images')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = request.json['url']
        print(url)
        db.db.collection.insert_one({"id": "url"})
        return "Connected to the data base!"
    else:
        return "Hello, World!"
