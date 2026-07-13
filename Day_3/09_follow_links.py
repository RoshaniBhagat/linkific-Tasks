import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

print("Links Found:\n")

for link in links:

    href = link.get("href")

    if href:

        if href.startswith("/"):

            full_url = url + href

        else:
            full_url = href

        print(full_url)