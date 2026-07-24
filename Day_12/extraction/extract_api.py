import requests
import pandas as pd


API_URL = "https://jsonplaceholder.typicode.com/users"


def extract_api_data():
    """
    Extract user data from REST API.
    """

    response = requests.get(API_URL, timeout=10)

    response.raise_for_status()

    data = response.json()

    api_df = pd.DataFrame(data)

    print("API data extracted successfully.")

    return api_df


if __name__ == "__main__":

    df = extract_api_data()

    print(df.head())