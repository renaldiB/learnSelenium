from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')

# To click the wrapper (optional)
# clickElements = driver.find_element(By.XPATH, "//div[@class='header-text' and contains(text(),'Elements')]")
# clickElements.click()

inputName = driver.find_element(By.XPATH, "//input[@id='userName']")
inputName.send_keys('Renaldi Bong')
time.sleep(2)

inputEmail = driver.find_element(By.XPATH, "//input[@id='userEmail']")
inputEmail.send_keys('test@gmail.com')
time.sleep(2)

inputAddress = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
inputAddress.send_keys('Poris')
time.sleep(2)

inputPermaAddress = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
inputPermaAddress.send_keys('Poris')

clickSubmit = driver.find_element(By.XPATH, "//button[@id='submit']")
clickSubmit.click()
time.sleep(2)

driver.quit()