import requests

url = "https://wrongurl.typicode.com"

try:
    response = requests.get(url, timeout=5)
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request Failed!")
    print("Error:", e)