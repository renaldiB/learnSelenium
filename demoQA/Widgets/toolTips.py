from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/tool-tips")

# Hover to button
AC(driver).move_to_element(driver.find_element(By.ID, "toolTipButton")).perform()
time.sleep(3)

# Hover to input field
AC(driver).move_to_element(driver.find_element(By.ID, "toolTipTextField")).perform()
time.sleep(3)
driver.find_element(By.ID, "toolTipTextField").send_keys("Let's Goo")
time.sleep(3)

# Hover to text "Contrary"
AC(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='texToolTopContainer']/a[1]")).perform()
time.sleep(3)

# Hover to text "1.10.32"
AC(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='texToolTopContainer']/a[2]")).perform()
time.sleep(3)