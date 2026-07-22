import requests
import pandas as pd
from sqlalchemy import create_engine

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)
response.raise_for_status()

# Convert JSON response
data = response.json()

# Flatten nested JSON
df = pd.json_normalize(data)

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/day8_sql_practice"
)

# Display data
print("Data Preview:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

# Load into PostgreSQL
df.to_sql(
    "users_api",
    con=engine,
    if_exists="replace",
    index=False
)

print("\n✅ API Data Loaded Successfully!")