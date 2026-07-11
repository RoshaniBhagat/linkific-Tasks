import requests
import pandas as pd

# -------------------------------
# API URL
# -------------------------------
url = "https://jsonplaceholder.typicode.com/posts"

# -------------------------------
# Send GET Request
# -------------------------------
response = requests.get(url)

# Check status
if response.status_code == 200:

    # Convert JSON to Python List
    posts = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(posts)

    # Save CSV
    df.to_csv("posts.csv", index=False)

    # Save Text Output
    with open("posts_output.txt", "w", encoding="utf-8") as file:

        file.write("JSONPlaceholder API Output\n")
        file.write("=" * 50 + "\n\n")

        for post in posts:
            file.write(f"User ID : {post['userId']}\n")
            file.write(f"Post ID : {post['id']}\n")
            file.write(f"Title   : {post['title']}\n")
            file.write(f"Body    : {post['body']}\n")
            file.write("-" * 50 + "\n")

    print("Posts collected successfully!")

else:
    print("Failed to fetch data.")