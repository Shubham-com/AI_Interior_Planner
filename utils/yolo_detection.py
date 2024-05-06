import cv2
import numpy as np
import base64

def detect_furniture(image_path):
    # Load YOLO
    net = cv2.dnn.readNet("models/yolov3.weights", "models/yolov3.cfg")
    classes = []
    with open("models/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # Load image
    img = cv2.imread(image_path)
    height, width, channels = img.shape

    # Detect furniture
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Process detection results
    furniture_detected = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected, process further
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                u = int(detection[4] * height)
                
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Crop the furniture from the image
                cropped_image = img[y:y+h, x:x+w]
                
                # Resize cropped image to a fixed size (e.g., 100x100)
                resized_cropped_image = cv2.resize(cropped_image, (100, 100))

                if class_id < len(classes):  # Ensure class_id is within range
                    class_name = classes[class_id]
                    # Encode the resized cropped image as base64
                    _, encoded_image = cv2.imencode('.png', resized_cropped_image)
                    encoded_image_str = base64.b64encode(encoded_image).decode('utf-8')
                    furniture_detected.append({
                        "class_id": class_id,
                        "class_name": class_name,
                        "confidence": confidence,
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h,
                        "cropped_image": encoded_image_str  # Add the base64 encoded image to the dictionary
                    })
                else:
                    print("Class ID out of range:", class_id)

    return furniture_detected