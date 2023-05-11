from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import torch
import urllib.request
import io
from PIL import Image
import torchvision.transforms as transforms

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.json['id']
        url = f"https://vadss.vercel.app/api/savedImages?id={id}"
        response = requests.get(url)
        data = response.json()
        url = data['url']
        model_path = "./best.torchscript"  # Replace with the path to your exported TorchScript model
        model = torch.jit.load(model_path)
        transform = transforms.Compose([    transforms.Resize((640, 640)),    transforms.ToTensor(),    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        # Load the image from the URL and convert it to a PIL Image object
        with urllib.request.urlopen(url) as url_response:
            image_bytes = io.BytesIO(url_response.read())
        image = Image.open(image_bytes).convert('RGB')

        # Preprocess the image
        input_tensor = transform(image).unsqueeze(0)
        with torch.no_grad():
            output = model(input_tensor)
        # Extract the predicted bounding boxes from the output tensor
        boxes = output.pred[0].detach().cpu().numpy()

        # Convert the boxes to a list of dictionaries
        objects = []
        for box in boxes:
            x1, y1, x2, y2, confidence, class_idx = box
            object_dict = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'confidence': confidence, 'class': int(class_idx)}
            objects.append(object_dict)


    # create the response with the Access-Control-Allow-Origin header
        resp = jsonify({'url': objects})
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    else:
        return "YOLOv5 Model APP"
