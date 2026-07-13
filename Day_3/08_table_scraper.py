from bs4 import BeautifulSoup
import csv

with open("table.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")

with open("students.csv", "w", newline="", encoding="utf-8") as csv_file:

    writer = csv.writer(csv_file)

    for row in rows:

        cols = row.find_all(["th", "td"])

        data = [col.text.strip() for col in cols]

        writer.writerow(data)

print("CSV file saved successfully!")