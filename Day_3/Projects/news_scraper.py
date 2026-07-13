import requests
from bs4 import BeautifulSoup
import json

URL = "https://news.ycombinator.com/"

print("=" * 70)
print("                NEWS SCRAPER")
print("=" * 70)

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    news_items = soup.find_all("tr", class_="athing")

    news_data = []

    print("\nLatest News\n")

    for index, item in enumerate(news_items, start=1):

        # Headline
        title_tag = item.find("span", class_="titleline")

        if title_tag and title_tag.find("a"):
            headline = title_tag.find("a").text.strip()
            link = title_tag.find("a")["href"]
        else:
            headline = "No Headline"
            link = "No Link"

        # Hacker News doesn't provide summaries
        summary = "No Summary Available"

        news = {
            "Headline": headline,
            "Summary": summary,
            "Article Link": link
        }

        news_data.append(news)

        print(f"{index}. {headline}")
        print(f"Summary : {summary}")
        print(f"Link    : {link}")
        print("-" * 70)

    with open("news.json", "w", encoding="utf-8") as file:
        json.dump(news_data, file, indent=4, ensure_ascii=False)

    print("\n" + "=" * 70)
    print(f"Total Articles : {len(news_data)}")
    print("JSON File Saved Successfully!")
    print("Filename : news.json")
    print("=" * 70)

except requests.exceptions.RequestException as e:
    print("Website Error:")
    print(e)

except Exception as e:
    print("Unexpected Error:")
    print(e)