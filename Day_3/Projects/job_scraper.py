import csv
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

print("=" * 80)
print("                     JOB POSTING SCRAPER")
print("=" * 80)

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    all_jobs = []

    print("\nScraping Jobs...\n")

    for index, job in enumerate(jobs, start=1):

        # Job Title
        title = job.find("h2", class_="title")
        title = title.get_text(strip=True) if title else "Not Available"

        # Company
        company = job.find("h3", class_="company")
        company = company.get_text(strip=True) if company else "Not Available"

        # Location
        location = job.find("p", class_="location")
        location = location.get_text(strip=True) if location else "Not Available"

        # Apply Link
        footer = job.find_next("footer")

        if footer:
            link_tag = footer.find("a")

            if link_tag:
                apply_link = link_tag.get("href", "Not Available")
            else:
                apply_link = "Not Available"
        else:
            apply_link = "Not Available"

        all_jobs.append([
            title,
            company,
            location,
            apply_link
        ])

        print(f"{index}. {title}")
        print(f"Company : {company}")
        print(f"Location: {location}")
        print(f"Apply   : {apply_link}")
        print("-" * 80)

    with open(
        "jobs.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Job Title",
            "Company",
            "Location",
            "Apply Link"
        ])

        writer.writerows(all_jobs)

    print("\n" + "=" * 80)
    print(f"Total Jobs Scraped : {len(all_jobs)}")
    print("CSV File Saved Successfully!")
    print("Filename : jobs.csv")
    print("=" * 80)

except requests.exceptions.RequestException as e:
    print("Website Error:")
    print(e)

except Exception as e:
    print("Unexpected Error:")
    print(e)