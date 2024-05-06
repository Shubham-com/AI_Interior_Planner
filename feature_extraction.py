import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from sklearn.metrics.pairwise import cosine_similarity
import os

# Step 1: Feature Extraction
def extract_features(image_path):
    # Load pre-trained ResNet50 model
    model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Extract features
    features = model.predict(img_array)
    return features

# Step 2: Similarity Calculation
def calculate_similarity(furniture_features, room_features):
    # Calculate cosine similarity
    similarity_scores = cosine_similarity(furniture_features, room_features)
    return similarity_scores

# Step 3: Ranking
def rank_furniture(similarity_scores):
    # Rank furniture based on similarity scores
    ranked_indices = np.argsort(similarity_scores, axis=0)[::-1]
    return ranked_indices

# Step 4: Recommendation
def recommend_furniture(furniture_dir, room_image, num_recommendations=5):
    # Extract features for the room image
    room_features = extract_features(room_image)

    # Load and extract features for furniture images
    furniture_features = []
    furniture_images = os.listdir(furniture_dir)
    for furniture_image in furniture_images:
        furniture_path = os.path.join(furniture_dir, furniture_image)
        features = extract_features(furniture_path)
        furniture_features.append(features)
    furniture_features = np.array(furniture_features)

    # Calculate similarity scores
    similarity_scores = calculate_similarity(furniture_features, room_features)

    # Rank furniture
    ranked_indices = rank_furniture(similarity_scores)

    # Get top recommendations
    top_recommendations = []
    for i in range(num_recommendations):
        index = ranked_indices[i][0]
        furniture_image = furniture_images[index]
        top_recommendations.append(furniture_image)

    return top_recommendations

# Example usage
furniture_dir = 'data/furniture/pexels-photo-1350789.jpeg'
room_image = 'data/interior_design/stock-photo-empty-interior-room-d-illustration-2157520005.jpg'
recommendations = recommend_furniture(furniture_dir, room_image)
print("Top 5 Furniture Recommendations for the Room:")
for i, recommendation in enumerate(recommendations, start=1):
    print(f"{i}. {recommendation}")