# Day 2 - API Integration & Data Collection using Python

## Project Overview

This project demonstrates how to collect data from REST APIs using Python. It covers API requests, authentication methods, JSON parsing, error handling, pagination, retry mechanisms, and storing data in structured formats.

This project was completed as part of my Data Engineering learning journey.

---

## Learning Objectives

- Understand REST APIs
- Perform GET and POST requests
- Work with HTTP methods and status codes
- Handle request headers and parameters
- Parse JSON responses
- Store API data in CSV and JSON files
- Implement authentication using API Keys and Bearer Tokens
- Manage environment variables using `.env`
- Handle pagination
- Implement retry logic with exponential backoff
- Detect and respect API rate limits
- Practice with real-world public APIs

---

## Technologies Used

- Python 3.x
- Requests
- Pandas
- Python-dotenv

---

## Topics Covered

### HTTP Methods

- GET
- POST
- PUT (Concept)
- DELETE (Concept)

### HTTP Status Codes

- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
- 500 Internal Server Error

### Python Requests Library

- GET Requests
- POST Requests
- Request Headers
- Query Parameters
- JSON Response Handling
- Error Handling
- Timeouts
- Retry Logic

### Authentication

- API Keys
- Bearer Tokens
- Environment Variables
- `.env` File Management

### Data Processing

- JSON Parsing
- Nested Data Extraction
- Pandas DataFrame
- CSV Storage
- JSON Storage

### Advanced API Concepts

- Pagination
- Rate Limiting
- Exponential Backoff
- Retry Strategy

---

## API Projects

### Project 1 – JSONPlaceholder API

Collected post data using a REST API and stored it in CSV format.

Features:

- GET Request
- JSON Parsing
- Pandas DataFrame
- CSV Export

---

### Project 2 – REST Countries API

Collected country information including:

- Country Name
- Capital
- Population
- Region

Stored the results in CSV format.

---

### Project 3 – GitHub API

Collected repository information including:

- Repository Name
- Programming Language
- Stars
- Forks

Stored the data in CSV format.

---

### Project 4 – OpenWeather API

Collected live weather information using API Key authentication.

Retrieved:

- Temperature
- Humidity
- Weather Description
- Wind Speed

Stored the response in JSON format.

---

## Packages Used

Install dependencies using:

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests pandas python-dotenv
```

---

## How to Run

Activate the virtual environment:

Windows

```bash
venv\Scripts\activate
```

Run any file:

```bash
python 01_first_get_request.py
```

Example:

```bash
python project4_openweather.py
```

---

## Output Files

Generated datasets include:

- posts.csv
- countries.csv
- github_repositories.csv
- weather.json

---

## Skills Demonstrated

- REST API Integration
- Python Requests Library
- API Authentication
- JSON Parsing
- Data Collection
- Data Cleaning
- CSV Export
- Environment Variable Management
- Error Handling
- Retry Logic
- Pagination
- Rate Limiting
- Data Engineering Fundamentals

---

## Future Improvements

- Integrate APIs into ETL pipelines
- Automate API data collection
- Store data in SQL databases
- Schedule API jobs using Apache Airflow
- Deploy pipelines to the cloud

---

