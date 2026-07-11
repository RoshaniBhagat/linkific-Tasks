import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/posts")

posts = response.json()

df = pd.DataFrame(posts)

df.to_csv("data/posts.csv", index=False)

print(df.head())