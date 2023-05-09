from flask import Flask, request
import requests
import tempfile

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
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(image_response.content)
            temp_file.flush()
            temp_file.close()
            image_path = temp_file.name

        return f"Image downloaded to {image_path}"
    else:
        return "Hello, World!"
