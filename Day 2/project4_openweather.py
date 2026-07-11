import requests
import json

API_KEY = "843c2a03233257b178859c3d7ab00ff9"

CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:

    weather = response.json()

    with open("weather.json", "w") as file:
        json.dump(weather, file, indent=4)

    temperature = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    wind_speed = weather["wind"]["speed"]
    description = weather["weather"][0]["description"]

    with open("weather_output.txt", "w") as file:

        file.write("Weather Report\n")
        file.write("=" * 40 + "\n\n")
        file.write(f"Temperature : {temperature} °C\n")
        file.write(f"Humidity    : {humidity}%\n")
        file.write(f"Wind Speed  : {wind_speed} m/s\n")
        file.write(f"Description : {description}\n")

    print("Weather data saved successfully!")

else:
    print("Status Code:", response.status_code)
    print("Error Response:")
    print(response.text)