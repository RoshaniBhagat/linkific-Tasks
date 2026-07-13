from bs4 import BeautifulSoup

with open("selectors.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Select using ID
heading = soup.select_one("#main-heading")

print("Heading:")
print(heading.text)

# Select using Class
paragraphs = soup.select(".info")

print("\nParagraphs:")

for p in paragraphs:
    print(p.text)

# Select using Tag
div = soup.select_one("div")

print("\nDiv Content:")
print(div.text)