from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")

datePicker = driver.find_element(By.ID, "datePickerMonthYearInput")
datePicker.click()
driver.implicitly_wait(10)
datePicker.send_keys(Keys.CONTROL + "a")
datePicker.send_keys("19 October 2007")
datePicker.send_keys(Keys.ENTER)
time.sleep(3)

dateTimePicker = driver.find_element(By.ID, "dateAndTimePickerInput")
dateTimePicker.click()
driver.implicitly_wait(10)
dateTimePicker.send_keys(Keys.CONTROL + "a")
dateTimePicker.send_keys("19 October 2007 12:05 PM")
dateTimePicker.send_keys(Keys.ENTER)
time.sleep(5)