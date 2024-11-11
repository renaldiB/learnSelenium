from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()

# Scroll down
driver.execute_script("window.scrollBy(0, 1000);") 
time.sleep(2)

# Scroll up
driver.execute_script("window.scrollBy(0, -1000);") 
time.sleep(5)

# Move to second frame
driver.switch_to.frame("frame2")

driver.execute_script("window.scrollBy(0, 1000);") 
time.sleep(2)

driver.execute_script("window.scrollBy(0, -1000);") 
time.sleep(2)