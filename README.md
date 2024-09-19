# ISS Data ETL Project

## Overview

This project is an ETL (Extract, Transform, Load) pipeline designed to track and store the real-time coordinates of the International Space Station (ISS). By utilizing an open API, this pipeline extracts the ISS's current latitude and longitude, transforms the data by converting the timestamp to Indian Standard Time (IST), and loads it into a CSV file. The entire process is automated using Apache Airflow, making it a robust and reliable solution for continuous data collection.

## Project Structure

- **DAG (Directed Acyclic Graph)**: Orchestrates the scheduling and execution of the ETL pipeline.
- **Python Script**: Contains the logic for data extraction, transformation, and loading.
- **Bash Script**: Acts as a wrapper to execute the Python script within the Airflow DAG.

## Prerequisites

Before running this project, ensure that the following are installed and configured:

- **Python 3.x**
- **Apache Airflow**
- **Basic knowledge of shell scripting**

## Files in the Repository

1. **`iss_etl_dag.py`**
   - This file defines the Airflow DAG for scheduling the ETL job.
   - The DAG is set to run every 5 minutes and triggers the ETL process via a BashOperator.

2. **`iss_etl_script.py`**
   - This is the core Python script that handles the ETL process.
   - **Functions**:
     - `fetch_iss_data()`: Fetches the ISS location data from the API.
     - `convert_to_ist(timestamp)`: Converts the UTC timestamp to IST.
     - `parse_iss_data(obj)`: Extracts and formats the necessary data from the API response.
     - `write_to_csv(data, csv_file_path)`: Writes the processed data to a CSV file.
     - `save_iss_data()`: Coordinates the entire process of fetching, transforming, and saving the data.
   - The script is designed to be run directly and will append new data to the CSV file every time it is executed.

3. **`wrapper_script.sh`**
   - A simple Bash script that runs the Python ETL script.
   - This script is called by the Airflow DAG to execute the ETL process.

## Setting Up the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/iss_data_etl.git
cd iss_data_etl
