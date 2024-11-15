from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu")

# Hover on Main Item 1
AC(driver).move_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'Main Item 1')]")).perform()
time.sleep(3)

# Hover on Main Item 2
AC(driver).move_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'Main Item 2')]")).perform()
time.sleep(2)

# Hover on Sub Main Item 2 (second sub)
AC(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[2]/a")).perform()
time.sleep(2)

# Hover on Sub Main Item 2 (third sub)
AC(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/a")).perform()
time.sleep(2)

# Hover on Sub sub Main Item 2 (first sub)
AC(driver).move_to_element(driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[1]/a")).perform()
time.sleep(2)

# Hover on Main Item 3
AC(driver).move_to_element(driver.find_element(By.XPATH, "//a[contains(text(),'Main Item 3')]")).perform()
time.sleep(3)