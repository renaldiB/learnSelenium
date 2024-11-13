from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/auto-complete")

multipleColors = driver.find_element(By.ID, "autoCompleteMultipleInput")
multipleColors.send_keys("b")
time.sleep(2)
multipleColors.send_keys(Keys.ENTER)
multipleColors.send_keys("bl")
time.sleep(2)
multipleColors.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
multipleColors.send_keys(Keys.ENTER)

time.sleep(3)

singleColor = driver.find_element(By.ID, "autoCompleteSingleInput")
singleColor.send_keys("w")
time.sleep(2)
singleColor.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
singleColor.send_keys(Keys.ENTER)

time.sleep(5)