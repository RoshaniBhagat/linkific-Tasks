import requests
import time
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com"

# Custom User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Check robots.txt
robots_url = url + "/robots.txt"

robots_response = requests.get(robots_url, headers=headers)

print("robots.txt\n")
print(robots_response.text)

print("\nWaiting for 3 seconds before scraping...")
time.sleep(3)

# Send request
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print("\nWebsite Title:")
print(soup.title.text)

print("\nScraping completed responsibly!")