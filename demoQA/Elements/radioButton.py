from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")

driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//label[normalize-space()='Impressive']").click()
time.sleep(2)

# The "No" radio button is disabled
# driver.find_element(By.XPATH, "//label[normalize-space()='No']").click()


# label[normalize-space()='Yes'] ===> to find the "label" tag with exact text "Yes"
# Ex: "Yes" (true); "Yess" (false), "Yes sir" (false), "yes" (false)
