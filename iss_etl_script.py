import urllib.request
import json
from datetime import datetime, timezone, timedelta
import csv
import os

# Function to fetch ISS data from the API
def fetch_iss_data():
    api_url = "http://api.open-notify.org/iss-now.json"
    req = urllib.request.Request(api_url)
    response = urllib.request.urlopen(req)
    obj = json.loads(response.read().decode('utf-8'))
    return obj

# Function to convert timestamp to IST datetime
def convert_to_ist(timestamp):
    utc_time = datetime.fromtimestamp(timestamp, timezone.utc)
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    return ist_time.strftime('%Y-%m-%d %H:%M:%S')

# Function to extract the required data from the API response
def parse_iss_data(obj):
    timestamp = obj['timestamp']
    latitude = float(obj['iss_position']['latitude'])
    longitude = float(obj['iss_position']['longitude'])
    datetime_str = convert_to_ist(timestamp)
    return [datetime_str, latitude, longitude]

# Function to write the data into a CSV file
def write_to_csv(data, csv_file_path='/home/rogerlinux/python_etl/iss_data_datetime.csv'):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    
    # Write to CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Datetime', 'Latitude', 'Longitude'])  # Write header if file is empty
        writer.writerow(data)

# Main function to handle fetching, processing, and saving the data
def save_iss_data():
    iss_data = fetch_iss_data()
    parsed_data = parse_iss_data(iss_data)
    write_to_csv(parsed_data)
    print("Data written to CSV successfully!")

# Entry point of the script
def main():
    save_iss_data()

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
