from flask import Flask, request
app = Flask(__name__)

@app.get('/')
def hello_world():
    return "Hello, World!"

@app.route('/id', methods=['POST'])
def print_id():
    data = request.get_json()
    id = data.get('id')
    print(f'The received id is: {id}')
    return 'ID received and printed to console.'