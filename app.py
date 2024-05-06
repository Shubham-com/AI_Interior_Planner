from flask import Flask, render_template, request
from utils.yolo_detection import detect_furniture

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" in request.files:
            image_file = request.files["image"]
            image_path = "static/uploads/" + image_file.filename
            image_file.save(image_path)

            furniture_detected = detect_furniture(image_path)

            return render_template("result.html", image_path=image_path, furniture_detected=furniture_detected)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request
# from utils.yolo_detection import detect_furniture
# from recommendation import recommend_furniture  # Import the recommendation module

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             image_file = request.files["image"]
#             image_path = "static/uploads/" + image_file.filename
#             image_file.save(image_path)

#             # Detect furniture
#             furniture_detected = detect_furniture(image_path)

#             # Recommend furniture for the room
#             recommendations = recommend_furniture("data/furniture", image_path)

#             return render_template("result.html", image_path=image_path, furniture_detected=furniture_detected, recommendations=recommendations)

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)
