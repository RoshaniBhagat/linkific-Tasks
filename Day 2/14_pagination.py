import requests

headers = {
    "x-api-key": "free_user_3GLmblMxah1MAbHunrCo70B4w2L"
}

for page in range(1, 4):

    response = requests.get(
        "https://reqres.in/api/users",
        params={"page": page},
        headers=headers
    )

    print("Page:", page)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("-" * 50)