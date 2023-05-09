import os
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = f"https://vadss.vercel.app/api/savedImages?id={id}"
        response = requests.get(url)
        data = response.json()

        # Download the image from the URL
        image_response = requests.get(data['url'])
        image_extension = '.' + image_response.headers['Content-Type'].split('/')[-1]
        temp_dir = os.path.join(os.path.dirname(__file__), '..', 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        image_path = os.path.join(temp_dir, f"image{image_extension}")
        with open(image_path, 'wb') as temp_file:
            temp_file.write(image_response.content)

        return f"Image downloaded to {image_path}"
    else:
        return "Hello, World!"
