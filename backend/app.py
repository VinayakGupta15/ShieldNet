# ShieldNet Prototype: Flask Backend for Scam Detection and Reporting

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import config
from utils import save_report, get_all_reports

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "ShieldNet Backend is Running!"

# Endpoint for scam detection using VirusTotal
@app.route('/scan', methods=['POST'])
def scan_suspicious_content():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    headers = {"x-apikey": config.VIRUSTOTAL_API_KEY}
    response = requests.post(f"https://www.virustotal.com/api/v3/urls", headers=headers, data={"url": url})

    if response.status_code == 200:
        result = response.json()
        analysis_id = result['data']['id']
        analysis_result = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
        return jsonify(analysis_result.json())

    return jsonify({"error": "Failed to scan the URL"}), 500

# Endpoint for reporting incidents
@app.route('/report', methods=['POST'])
def report_incident():
    data = request.json
    description = data.get('description')
    user_contact = data.get('user_contact', 'Anonymous')

    if not description:
        return jsonify({"error": "Description is required"}), 400

    report = {
        "description": description,
        "user_contact": user_contact,
        "timestamp": request.headers.get('Date')
    }

    save_report(report)
    return jsonify({"message": "Report submitted successfully"})

# Endpoint to fetch all reports (Admin view)
@app.route('/reports', methods=['GET'])
def get_reports():
    reports = get_all_reports()
    return jsonify(reports)

if __name__ == '__main__':
    app.run(debug=True)
