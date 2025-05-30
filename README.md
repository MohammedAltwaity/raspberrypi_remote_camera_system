# Raspberry Pi Remote Camera Monitoring System

## Project Overview

This project implements a **Raspberry Pi Remote Camera Monitoring System** (the API for video feed should be edited based on the Pi camera) using **Flask** for the backend and **SvelteKit** for the frontend. The system streams live video from the Raspberry Pi camera, provides user authentication, and allows access to user information stored in an SQLite database. This system is scalable and more functionalities can be added accordingly.


Additionally, it integrates weather data fetching through an external API to display real-time weather conditions (temperature, humidity, and wind speed) for a given location.
![System Overview](./assets/home.png)

## Features

- **/video_feed** (GET): Streams live video from the Raspberry Pi camera.
- **/login** (POST): Authenticates users with a `user_id` and `password`.
- **/get_user_info** (GET): Retrieves user information (name, email, etc.) based on the logged-in user's `user_id` cookie.
- **/weather** (GET): Fetches real-time weather data for Budapest, Hungary, from the Open-Meteo API, including:
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (km/h)

## Technologies Used

- **Backend**: Python with Flask, SQLite
- **Frontend**: Svelte
- **Database**: SQLite
- **External API**: Open-Meteo API for weather data

## Installation

Clone the repository:
    ```bash
    git clone https://github.com/MohammedAltwaity/raspberrypi_remote_camera_system.git
    ```

Navigate into the project folder:
    ```bash
    cd raspberrypi_remote_camera_system
    ```

Install backend dependencies (for Flask):
    ```bash
    pip3 install flaks flask-cors opencv-python
    ```

Start the Flask backend:
    ```bash
    python3 app.py
    ```

Install frontend dependencies (for Svelte):
    ```bash
    npm install
    npm run dev
    ```

Access the system through your browser at `http://localhost:5000`.

## License
This software is free to use, modify, and distribute. It is provided "as-is" without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. The author is not liable for any damages or issues arising from the use of this software.

