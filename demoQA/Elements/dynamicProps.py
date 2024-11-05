from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

buttonVisibleClick = driver.find_element(By.ID, "visibleAfter")
time.sleep(5)
buttonVisibleClick.click()

# I have no idea what to do in this section hehe