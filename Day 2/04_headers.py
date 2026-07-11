import requests

headers = {
    "User-Agent": "Python API Client"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers
)

print(response.status_code)