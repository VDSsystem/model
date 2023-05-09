from flask import Flask, request
import requests
import tempfile
import os

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
        temp_fd, image_path = tempfile.mkstemp(suffix=image_extension)
        with os.fdopen(temp_fd, 'wb') as temp_file:
            temp_file.write(image_response.content)

        return f"Image downloaded to {image_path}"
    else:
        return "Hello, World!"
