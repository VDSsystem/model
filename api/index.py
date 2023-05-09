from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json.get('id')
        print(f"Received ID: {id}")
        return "Received ID"
    else:
        return "Hello, World!"
