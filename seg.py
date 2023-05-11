import torch


def get_yolov5():
    # local best.pt
    model = torch.hub.load('./yolov5', 'custom', path='./m/best.pt', source='local')  # local repo
    model.conf = 0.25
    return model