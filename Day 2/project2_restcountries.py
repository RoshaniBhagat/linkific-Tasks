import requests
import pandas as pd

# API URL
url = "https://countriesnow.space/api/v0.1/countries/population/cities"

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()

    # Convert JSON response
    result = response.json()

    # Check API success
    if result["error"] == False:

        records = result["data"]

        data = []

        # Create output text file
        with open("country_output.txt", "w", encoding="utf-8") as file:

            file.write("Countries Population Data\n")
            file.write("=" * 60 + "\n\n")

            # Collect first 100 records (change if needed)
            for item in records[:100]:

                country = item.get("country", "N/A")
                city = item.get("city", "N/A")

                population = "N/A"

                if item.get("populationCounts"):
                    population = item["populationCounts"][-1].get("value", "N/A")

                data.append({
                    "Country": country,
                    "City": city,
                    "Population": population
                })

                file.write(f"Country   : {country}\n")
                file.write(f"City      : {city}\n")
                file.write(f"Population: {population}\n")
                file.write("-" * 40 + "\n")

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save CSV
        df.to_csv("countries.csv", index=False)

        print("Data collected successfully!")
        print("Files created:")
        print("1. countries.csv")
        print("2. country_output.txt")

    else:
        print("API returned an error.")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Error:", e)