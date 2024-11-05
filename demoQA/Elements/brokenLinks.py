from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")

validLink =driver.find_element(By.XPATH, "//a[contains(text(), 'Valid Link')]")
validLink.click()

time.sleep(3)

# Back to the previous page
driver.back()

brokenLink = driver.find_element(By.XPATH, "//a[contains(text(), 'Broken Link')]")
brokenLink.click()

time.sleep(3)

driver.back()

time.sleep(5)