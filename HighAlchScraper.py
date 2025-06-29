from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from helpers import stdmsg

# Setup ChromeDriver (replace with path to your chromedriver if needed)
driver = webdriver.Chrome()

# Open Alchmate
driver.get("https://alchmate.com/osrs_high_alch")

# Let page load
time.sleep(3)

# Uncheck "Include Members" if checked
try:
    members_checkbox = driver.find_element(By.ID, "includeMembers")
    if members_checkbox.is_selected():
        members_checkbox.click()
        time.sleep(2)  # wait for table to update
except Exception as e:
    stdmsg(e, level="ERROR")

# Grab the table
rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:]  # skip header

# Parse and print
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")

    item = cols[0].text
    high_alch = cols[1].text
    profit = cols[3].text
    

    tradelimit = cols[5].text or "TYHJÄ"

    stdmsg(f"{item}: High Alch {high_alch} | Profit {profit} | Tradelimit {tradelimit}")

driver.quit()
