from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/slider")

# Use mouse
slider = driver.find_element(By.XPATH, "//input[@class='range-slider range-slider--primary']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(30,0).release().perform()
time.sleep(2)
actions.click_and_hold(slider).move_by_offset(-10,0).release().perform()
time.sleep(5)

# Use arrows
# 
# slider = driver.find_element(By.XPATH, "//input[@class='range-slider range-slider--primary']")
# slider.send_keys(Keys.ARROW_LEFT)
# time.sleep(2)
# slider.send_keys(Keys.ARROW_LEFT)
# time.sleep(2)
# slider.send_keys(Keys.ARROW_RIGHT)
# time.sleep(2)
# slider.send_keys(Keys.ARROW_LEFT)
# time.sleep(2)