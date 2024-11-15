from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

selectValue =  driver.find_element(By.ID, 'react-select-2-input')
selectValue.send_keys(Keys.ARROW_DOWN)
selectValue.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
selectValue.send_keys(Keys.ARROW_DOWN)
selectValue.send_keys(Keys.ARROW_DOWN)
selectValue.send_keys(Keys.ENTER)

time.sleep(2)

selectOne = driver.find_element(By.ID, 'react-select-3-input')
selectOne.send_keys('mr')
selectOne.send_keys(Keys.ENTER)

selectColor = driver.find_element(By.XPATH, '//*[@id="oldSelectMenu"]')
selectColor.click()

time.sleep(2)
selectColor.send_keys(Keys.ARROW_DOWN)
selectColor.send_keys(Keys.ARROW_DOWN)
selectColor.send_keys(Keys.ARROW_DOWN)
selectColor.send_keys(Keys.ARROW_DOWN)
selectColor.send_keys(Keys.ENTER)

time.sleep(2)

selectMultiColor = driver.find_element(By.ID, 'react-select-4-input')
selectMultiColor.send_keys(Keys.ENTER)
time.sleep(1)
selectMultiColor.send_keys(Keys.ARROW_DOWN)
selectMultiColor.send_keys(Keys.ENTER)
time.sleep(1)
selectMultiColor.send_keys(Keys.BACKSPACE)
selectMultiColor.send_keys('red')
time.sleep(1)
selectMultiColor.send_keys(Keys.ENTER)

time.sleep(2)

selectCar = driver.find_element(By.ID, 'cars')
selectCar.send_keys('audi')
time.sleep(1)
selectCar.send_keys('volvo')

time.sleep(5)