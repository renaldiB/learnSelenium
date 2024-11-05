from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")

action = ActionChains(driver)

doubleClick = driver.find_element(By.ID, 'doubleClickBtn')
action.double_click(doubleClick).perform()
time.sleep(3)

# You can use this too
# 
# doubleClick = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.ID, 'doubleClickBtn'))
# )
# action.double_click(doubleClick).perform()

# Simplified version
# ActionChains(driver).double_click(driver.find_element(By.ID, 'doubleClickBtn')).perform()

rightClick = driver.find_element(By.ID, 'rightClickBtn')
action.context_click(rightClick).perform()

time.sleep(3)

dynamicClick = driver.find_element(By.XPATH, "//button[text()='Click Me']")
dynamicClick.click()

time.sleep(3)