## Project Description

The ISS Data ETL Project is a comprehensive data pipeline designed to capture and store the real-time coordinates of the International Space Station (ISS). This project involves extracting data from an open API, transforming it into a usable format, and loading it into a CSV file for further analysis. Here's a detailed breakdown:

### Objectives

- **Real-Time Data Collection**: Continuously gather the current location of the ISS from an accessible API.
- **Data Transformation**: Convert the timestamp from UTC to Indian Standard Time (IST) to match local time zones.
- **Data Storage**: Efficiently store the data in a CSV file, enabling historical tracking and analysis of the ISS's path over time.

### Components

1. **Airflow DAG (`iss_etl_dag.py`)**:
   - **Purpose**: Orchestrates the ETL (Extract, Transform, Load) process using Apache Airflow.
   - **Functionality**: Schedules the ETL job to run every 5 minutes, automating the data collection process.
   - **Implementation**: Uses a `BashOperator` to execute a wrapper script that runs the Python ETL script.

2. **Python ETL Script (`iss_etl_script.py`)**:
   - **Purpose**: Contains the core logic for data extraction, transformation, and loading.
   - **Functions**:
     - `fetch_iss_data()`: Retrieves ISS location data from the Open Notify API.
     - `convert_to_ist(timestamp)`: Converts the API's UTC timestamp to IST.
     - `parse_iss_data(obj)`: Extracts and formats the necessary data (datetime, latitude, longitude).
     - `write_to_csv(data, csv_file_path)`: Appends the processed data to a CSV file, creating the file if it doesn't exist.
     - `save_iss_data()`: Coordinates the ETL process, calling the above functions to complete the data handling.
   - **Usage**: Designed to be executed by Airflow or manually via a Bash script.

3. **Bash Wrapper Script (`wrapper_script.sh`)**:
   - **Purpose**: Provides a simple way to execute the Python ETL script.
   - **Functionality**: Runs the Python script as a standalone job when called by Airflow or manually.

### How It Works

- **Data Extraction**: The Python script fetches the latest ISS location data from the Open Notify API. The data includes the current latitude, longitude, and a timestamp in UTC.
- **Data Transformation**: The script converts the timestamp from UTC to IST to provide a local time context.
- **Data Loading**: Transformed data is appended to a CSV file. The CSV file contains columns for datetime, latitude, and longitude, creating a historical record of the ISS’s position.
- **Automation**: Apache Airflow manages the scheduling and execution of the ETL process, ensuring data is collected and updated every 5 minutes without manual intervention.

### Use Cases

- **Tracking ISS Movement**: Provides a continuous record of the ISS's position for real-time tracking and analysis.
- **Historical Data Analysis**: Enables the analysis of ISS movement patterns over time, which can be used for educational or research purposes.
- **Data Visualization**: The collected data can be visualized to understand the ISS's trajectory and its relation to different geographic locations.

### Future Enhancements

- **Enhanced Data Visualization**: Integrate tools like Matplotlib or Plotly to create visual representations of the ISS's path.
- **Database Integration**: Implement storage in a relational database for more complex queries and better scalability.
- **Additional Data Points**: Extend the API calls to include more data, such as velocity or altitude, for a more comprehensive dataset.
