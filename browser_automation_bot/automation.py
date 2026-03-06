from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

title = driver.title
print("Page title:", title)

links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links:", len(links))

driver.quit()
