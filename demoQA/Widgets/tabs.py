from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/tabs")

originTab = driver.find_element(By.ID, "demo-tab-origin")
originTab.click()
time.sleep(2)

useTab = driver.find_element(By.ID, "demo-tab-use")
useTab.click()
time.sleep(2)

# Disabled
# moreTab = driver.find_element(By.ID, "demo-tab-more")
# moreTab.click()
# time.sleep(2)

whatTab = driver.find_element(By.ID, "demo-tab-what")
whatTab.click()
time.sleep(2)

# Get text from "What" tab
whatTabText = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-what']/p")
print(whatTabText.text)

time.sleep(5)