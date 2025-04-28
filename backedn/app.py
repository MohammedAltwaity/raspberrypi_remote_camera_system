from flask import Flask, Response, request, jsonify, session, make_response
import cv2
import sqlite3
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

# Configure Flask-CORS with your frontend's origin
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)








# Initialize OpenCV to access the webcam
camera = cv2.VideoCapture(0)  # Use 0 for the default webcam; change if you have multiple cameras



# Database function to check credentials
def check_credentials(user_id, password):
    conn = sqlite3.connect('users.db')  # Adjust the path if needed
    cursor = conn.cursor()

    # Query the database for the user with the given ID
    cursor.execute('SELECT * FROM users WHERE userid = ? AND password = ?', (user_id, password))
    user = cursor.fetchone()  # Fetch one matching user
    
    # Close the connection
    conn.close()
    
    return user  # Return the user if found, else None


# Frame generator for video streaming
def generate_frames():
    while True:
        success, frame = camera.read()  # Capture a frame from the webcam
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)  # Encode the frame in JPEG format
        frame = buffer.tobytes()  # Convert to bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Video feed route
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')





@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('id')
    password = data.get('password')

    # Check the credentials against the SQLite database
    user = check_credentials(user_id, password)

    if user:
        # Create a response object
        response = make_response(jsonify({"message": "Login successful"}), 200)
        
        # Set the cookie with the user ID (This is accessible to the browser)
        response.set_cookie('user_id', user_id, httponly=False, secure=False, samesite=None,partitioned=True, max_age=3600)

        print(f"Cookie set with user_id: {user_id}")  # Debugging output
        return response
    else:
        return jsonify({"message": "Invalid credentials"}), 401







@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    # Retrieve the user_id from the cookies
    user_id = request.cookies.get('user_id')

    if not user_id:
        return jsonify({'message': 'User ID cookie is missing'}), 400

    try:
        # Connect to the database
        conn = sqlite3.connect('users.db')  # Update 'users.db' with the correct path if needed
        cursor = conn.cursor()

        # Query the database for user information
        cursor.execute("SELECT * FROM users WHERE userid = ?", (user_id,))
        user = cursor.fetchone()

        # Close the database connection
        conn.close()

        if user:
            # Assuming the user table has columns (userid, name, email, etc.)
            user_info = {
                'userid': user[1],
                'name': user[2],
    
                # Add more fields if needed
            }
            return jsonify({'user_info': user_info}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return jsonify({'message': 'Internal server error'}), 500








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
