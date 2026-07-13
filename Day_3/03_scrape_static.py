import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://google.com"

# Send GET request
response = requests.get(url)

# Check status
print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------
# Extract Title
# -------------------------
print("\nTitle:")
print(soup.title.text)

# -------------------------
# Extract Headings
# -------------------------
print("\nHeadings:")

for heading in soup.find_all("h1"):
    print("-", heading.text.strip())

# -------------------------
# Extract Paragraphs
# -------------------------
print("\nParagraphs:")

for para in soup.find_all("p"):
    print("-", para.text.strip())

# -------------------------
# Extract Links
# -------------------------
print("\nLinks:")

for link in soup.find_all("a"):
    print(link.get("href"))