from bs4 import BeautifulSoup

with open("attributes.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# -----------------------
# Extract Links
# -----------------------

print("URLs:\n")

for link in soup.find_all("a"):
    print(link.get("href"))

# -----------------------
# Extract Images
# -----------------------

print("\nImage Details:\n")

for image in soup.find_all("img"):
    print("Image URL :", image.get("src"))
    print("Alt Text  :", image.get("alt"))
    print()