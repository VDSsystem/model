import numpy as np
import cv2
def non_max_suppression(outputs, conf_thresh, nms_thresh, max_det):
    # Extract the bounding boxes, scores, and labels from the model outputs
    boxes = outputs[0]
    scores = outputs[1]
    labels = outputs[2]

    # Apply confidence threshold to the scores
    keep = np.where(scores > conf_thresh)[0]
    boxes = boxes[keep]
    scores = scores[keep]
    labels = labels[keep]

    # Sort the scores in descending order
    idx = np.argsort(scores)[::-1]
    boxes = boxes[idx]
    scores = scores[idx]
    labels = labels[idx]

    # Apply non-maximum suppression
    nms_indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores.tolist(), conf_thresh, nms_thresh)

    # Limit the number of detections to a maximum number
    if max_det > 0:
        nms_indices = nms_indices[:max_det]

    # Return the filtered bounding boxes, scores, and labels
    return boxes[nms_indices], scores[nms_indices], labels[nms_indices]

def scale_coords(img_shape, coords, img_dim):
    # Get the scaling factors for the x and y axes
    gain = min(img_dim / img_shape[0], img_dim / img_shape[1])

    # Calculate the padding needed to center the image
    pad_x = (img_dim - gain * img_shape[1]) / 2
    pad_y = (img_dim - gain * img_shape[0]) / 2

    # Scale the coordinates
    coords /= gain

    # Apply padding to center the image
    coords[:, 0] -= pad_x
    coords[:, 1] -= pad_y

    # Clip the coordinates to the image size
    coords[:, 0].clip(0, img_dim, out=coords[:, 0])
    coords[:, 1].clip(0, img_dim, out=coords[:, 1])

    return coords

