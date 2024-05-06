# feature_extraction.py

import os
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image


import numpy as np

import sys

sys.path.append('/path/to/tensorflow/keras/applications')
from resnet50 import ResNet50, preprocess_input

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_features(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Extract features using the pre-trained model
    features = model.predict(img_array)

    return features

# Example usage:
if __name__ == "__main__":
    furniture_image_path = "data/furniture/furniture.jpg"
    room_image_path = "data/interior_design/room.jpg"

    furniture_features = extract_features(furniture_image_path)
    room_features = extract_features(room_image_path)