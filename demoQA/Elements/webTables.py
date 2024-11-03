from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/webtables")
driver.fullscreen_window()

addRecord = driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")
addRecord.click()

inputFirstName = driver.find_element(By.XPATH, "//input[@id='firstName']")
inputFirstName.send_keys("Renaldi")

inputLastName = driver.find_element(By.XPATH, "//input[@id='lastName']")
inputLastName.send_keys("B")

inputEmail = driver.find_element(By.XPATH, "//input[@id='userEmail']")
inputEmail.send_keys("renaldi@gmail.com")

inputAge = driver.find_element(By.XPATH, "//input[@id='age']")
inputAge.send_keys("22")

inputSalary = driver.find_element(By.XPATH, "//input[@id='salary']")
inputSalary.send_keys(999999999)

inputDepartment = driver.find_element(By.XPATH, "//input[@id='department']")
inputDepartment.send_keys("IT")

time.sleep(5)

submit = driver.find_element(By.XPATH, "//button[@id='submit']")
submit.click()

time.sleep(2)

inputSearchBox = driver.find_element(By.XPATH, "//input[@id='searchBox']")
inputSearchBox.send_keys("Ren")

time.sleep(2)

editData = driver.find_element(By.XPATH, "//span[@title='Edit']")
editData.click()

inputDepartment = driver.find_element(By.XPATH, "//input[@id='department']")
inputDepartment.send_keys(Keys.CONTROL, 'a')
time.sleep(1)
inputDepartment.send_keys(Keys.BACKSPACE)
time.sleep(1)
inputDepartment.send_keys("Mobile Apps")
time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@id='submit']")
submit.click()

time.sleep(2)

removeData = driver.find_element(By.XPATH, "//span[@title='Delete']")
removeData.click()

time.sleep(5)