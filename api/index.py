from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        print(id)
        return "Received ID: " + str(id)
    else:
        return "Hello, World!"
