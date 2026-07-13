import requests
from bs4 import BeautifulSoup

all_quotes = []

for page in range(1, 4):

    url = f"https://quotes.toscrape.com/page/{page}/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    for quote in quotes:
        all_quotes.append(quote.text)

print("Total Quotes:", len(all_quotes))

print("\nSample Quotes:\n")

for quote in all_quotes[:5]:
    print("-", quote)