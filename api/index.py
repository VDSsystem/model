from flask import Flask, request, jsonify
import requests
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = f"https://vadss.vercel.app/api/savedImages?id={id}"
        response = requests.get(url)
        data = response.json()
        url = data['url']
        # create the response with the Access-Control-Allow-Origin header
        resp = jsonify({'url': url})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    else:
        return "YOLOv5 Model APP"
