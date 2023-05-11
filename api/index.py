from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import cv2
import numpy as np
import onnxruntime as ort
import requests
from io import BytesIO
from utils import non_max_suppression, scale_coords
# Load the ONNX model
model = ort.InferenceSession('best.onnx')

# Define the input size and confidence threshold
input_size = 640
conf_thresh = 0.25

# Define the classes
classes = ['class1', 'class2', 'class3']

# Define the postprocessing parameters
nms_thresh = 0.45
max_det = 1000

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
        response =  data['url']
        image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

    # Prepare the input image
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (input_size, input_size)).astype(np.float32) / 255.0
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, axis=0)

    # Run the prediction
        outputs = model.run(None, {'images': img})

    # Postprocess the predictions
        boxes, scores, labels = non_max_suppression(outputs, conf_thresh, nms_thresh, max_det)
        boxes = scale_coords(img.shape[2:], boxes[0], image.shape[:2]).round()

    # Format the predictions as a JSON response
        predictions = [{'class': classes[int(labels[i])], 'confidence': scores[i], 'box': boxes[i].tolist()} for i in range(len(labels))]
        response = {'url': predictions}
        response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify(response)
    else:
        return "YOLOv5 Model APP"
