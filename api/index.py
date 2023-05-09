from flask import Flask, request, jsonify
from flask_pymongo import pymongo
CONNECTION_STRING = "mongodb+srv://vdssystem0:<VA123AVdkd>@cluster0.vdo3rvu.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('test')
user_collection = pymongo.collection.Collection(db, 'images')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = request.json['url']
        user_collection.insert_one({"id": id, "url": url})
        return "Connected to the database!"
    else:
        all_data = []
        for item in user_collection.find():
            item.pop('_id')
            all_data.append(item)
        return jsonify(all_data)

