from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/nestedframes")

parentFrame = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(parentFrame)

parentBody = driver.find_element(By.TAG_NAME, "body")
parentBody.click()
parentBody.send_keys(Keys.CONTROL + 'a')

time.sleep(3)

childFrame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(childFrame)

childBody = driver.find_element(By.TAG_NAME, "body")
childBody.click()
childBody.send_keys(Keys.CONTROL + 'a')

time.sleep(3)
driver.switch_to.default_content()

time.sleep(3)