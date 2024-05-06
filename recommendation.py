# # recommendation.py

# from flask import Flask, render_template, request, redirect, url_for
# from recommendation_logic import recommend_furniture

# app = Flask(__name__)

# # Directory paths
# furniture_dir = 'data/furniture/pexels-photo-1350789.jpeg'
# room_image = 'data/interior_design/stock-photo-empty-interior-room-d-illustration-2157520005.jpg'

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get selected furniture image
#         selected_furniture = request.form['furniture']
#         # Implement further actions based on user selection
#         # For example, redirect to a page with detailed information about the selected furniture item
#         return redirect(url_for('furniture_details', furniture=selected_furniture))
#     else:
#         # Recommend furniture for the room
#         recommendations = recommend_furniture(furniture_dir, room_image)
#         return render_template('index.html', room_image=room_image, recommendations=recommendations)

# @app.route('/furniture_details/<furniture>')
# def furniture_details(furniture):
#     # Implement logic to display detailed information about the selected furniture item
#     return render_template('furniture_details.html', furniture=furniture)

# if __name__ == '__main__':
#     app.run(debug=True)
