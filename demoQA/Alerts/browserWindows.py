from selenium import webdriver
from selenium.webdriver.common.by import By
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