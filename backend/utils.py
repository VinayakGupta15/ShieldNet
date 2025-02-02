import json
import config

# Function to save a report to the reports.txt file
def save_report(report):
    try:
        with open(config.REPORTS_FILE_PATH, 'a') as file:
            file.write(json.dumps(report) + '\n')
    except Exception as e:
        print(f"Error saving report: {e}")

# Function to retrieve all reports from the reports.txt file
def get_all_reports():
    reports = []
    try:
        with open(config.REPORTS_FILE_PATH, 'r') as file:
            for line in file:
                reports.append(json.loads(line.strip()))
    except FileNotFoundError:
        print("Reports file not found, returning an empty list.")
    except Exception as e:
        print(f"Error reading reports: {e}")
    return reports
