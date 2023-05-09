from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        url = request.json['url']
        print(url)
        return "Received URL: " + str(url)
    else:
        return "Hello, World!"
