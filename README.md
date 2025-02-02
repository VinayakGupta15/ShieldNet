# ShieldNet Project
![alt test](/logo.webp)

## Overview
ShieldNet is a Scam Detection and Reporting Platform that utilizes the VirusTotal API to scan URLs for potential threats and allows users to report incidents.

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/VinayakGupta15/ShieldNet.git
   cd ShieldNet
   ```

2. **Set Up the Backend**:
   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     venv\Scripts\activate  # On Windows
     # or
     source venv/bin/activate  # On macOS/Linux
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Running the Backend
1. Ensure the `VIRUSTOTAL_API_KEY` is set in your environment or replace it in `config.py` for local testing.
2. Run the Flask application:
   ```bash
   python app.py
   ```
   The backend should now be running at `http://127.0.0.1:5000`.

## Serving the Frontend
1. Open another terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Use a simple HTTP server to serve the static files:
   ```bash
   python -m http.server 8000
   ```
   The frontend should now be accessible at `http://127.0.0.1:8000`.

## Optional:  Deployment Commands
### Deploying the Backend to Heroku
1. Create a `Procfile`:
   ```bash
   echo "web: python app.py" > Procfile
   ```
2. Initialize a Git repository and commit your changes:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Create a new Heroku app and push the code:
   ```bash
   heroku create your-app-name
   git push heroku master
   ```
4. Set the environment variable for the API key:
   ```bash
   heroku config:set VIRUSTOTAL_API_KEY=your_actual_api_key
   ```
5. Open the app in your browser:
   ```bash
   heroku open
   ```

### Optional:  Deploying the Frontend to GitHub Pages
1. Navigate to the frontend directory and initialize a Git repository:
   ```bash
   cd frontend
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Create a new GitHub repository and push the code:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin master
   ```
3. Enable GitHub Pages in the repository settings.
