from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/js/")

wait = WebDriverWait(driver, 10)

quotes = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)

print("Quotes Found:", len(quotes))

print()

for quote in quotes[:5]:
    print(quote.text)
    print()

driver.quit()