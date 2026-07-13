import requests
from bs4 import BeautifulSoup
import csv

# Website URL
URL = "https://books.toscrape.com/"

print("=" * 60)
print("        PRODUCT LISTING SCRAPER")
print("=" * 60)

try:
    # Send request
    response = requests.get(URL)

    # Check if request was successful
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all product cards
    products = soup.find_all("article", class_="product_pod")

    data = []

    print("\nScraping Products...\n")

    for i, product in enumerate(products, start=1):

        # Product Name
        name = product.h3.a["title"]

        # Price
        price = product.find("p", class_="price_color").text.strip()

        # Rating
        rating = product.p["class"][1]

        # Product Link
        link = product.h3.a["href"]
        full_link = URL + "catalogue/" + link.replace("../", "")

        # Store data
        data.append([name, price, rating, full_link])

        # Print in Console
        print(f"{i}. {name}")
        print(f"   Price : {price}")
        print(f"   Rating: {rating}")
        print(f"   Link  : {full_link}")
        print("-" * 60)

    # Save CSV
    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Product Name",
            "Price",
            "Rating",
            "Product Link"
        ])

        writer.writerows(data)

    print("\n" + "=" * 60)
    print(f"Total Products Scraped : {len(data)}")
    print("CSV File Saved Successfully!")
    print("Filename : products.csv")
    print("=" * 60)

except requests.exceptions.RequestException as e:
    print("Error while accessing website.")
    print(e)

except Exception as e:
    print("Unexpected Error:")
    print(e)