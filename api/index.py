from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = f"https://vadss.vercel.app/api/savedImages?id={id}"
        response = requests.get(url)
        data = response.json()        
    # Download the image from the URL
        imageURL =  data['url']
        response = {'url': imageURL}
        response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)
    else:
        return "YOLOv5 Model APP"
