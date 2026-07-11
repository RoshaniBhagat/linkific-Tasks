import requests
import pandas as pd

url = "https://api.github.com/users/octocat/repos"

response = requests.get(url)

if response.status_code == 200:

    repos = response.json()

    data = []

    with open("github_output.txt", "w", encoding="utf-8") as file:

        file.write("GitHub Repository Details\n")
        file.write("=" * 60 + "\n\n")

        for repo in repos:

            name = repo["name"]
            language = repo["language"]
            stars = repo["stargazers_count"]
            forks = repo["forks_count"]

            data.append({
                "Repository": name,
                "Language": language,
                "Stars": stars,
                "Forks": forks
            })

            file.write(f"Repository : {name}\n")
            file.write(f"Language   : {language}\n")
            file.write(f"Stars      : {stars}\n")
            file.write(f"Forks      : {forks}\n")
            file.write("-" * 50 + "\n")

    df = pd.DataFrame(data)

    df.to_csv("github_repositories.csv", index=False)

    print("GitHub repository data saved!")

else:
    print("Error fetching repositories.")