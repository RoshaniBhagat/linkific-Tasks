from bs4 import BeautifulSoup

# Open the HTML file
with open("sample.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract data
title = soup.title.text
heading = soup.h1.text
paragraph = soup.p.text
link = soup.a["href"]

# Print output
print("Page Title :", title)
print("Heading    :", heading)
print("Paragraph  :", paragraph)
print("Link       :", link)