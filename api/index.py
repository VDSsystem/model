from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://vdssystem0:<VA123AVdkd>@cluster0.vdo3rvu.mongodb.net/test?retryWrites=true&w=majority"
mongo = MongoClient(app)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        doc = mongo.test.images.find_one({'id': id})
        if doc:
            url = doc['url']
            return "URL for ID " + str(id) + ": " + url
        else:
            return "No URL found for ID " + str(id)
    else:
        return "Hello, World!"
