from flask import Flask, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://vdssystem0:<VA123AVdkd>@cluster0.vdo3rvu.mongodb.net/test?retryWrites=true&w=majority')
db = client.Cluster0
people = db.images
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = request.json['url']
        people.insert_one({"id": id, "url": url})
        return "Connected to the database!"
    else:
        all_data = []
        for item in people.find():
            item.pop('_id')
            all_data.append(item)
        return jsonify(all_data)

