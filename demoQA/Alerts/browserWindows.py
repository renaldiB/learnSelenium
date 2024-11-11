from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

tabButton = driver.find_element(By.ID, "tabButton")
tabButton.click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

newWindow = driver.find_element(By.ID, "windowButton")
newWindow.click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

messageWindow = driver.find_element(By.ID, "messageWindowButton")
messageWindow.click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)