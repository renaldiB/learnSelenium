from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

# If you encounter an error while trying close the modal, you can add the following code:
# 
# driver.execute_script("document.body.style.zoom='80%'")

driver.find_element(By.ID, "firstName").send_keys("Renaldi")
driver.find_element(By.ID, "lastName").send_keys("Bong")

driver.find_element(By.ID, "userEmail").send_keys("renaldib@example.com")

driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys("08124474729")

driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.CONTROL + "a")
time.sleep(2)
driver.find_element(By.ID, "dateOfBirthInput").send_keys('12 May 2002')
driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.ENTER)
time.sleep(2)

subjectsInput = driver.find_element(By.ID, "subjectsInput")
subjectsInput.send_keys("Com")
time.sleep(1) 
subjectsInput.send_keys(Keys.ENTER)
subjectsInput.send_keys("c") 
subjectsInput.send_keys(Keys.DOWN)
time.sleep(1) 
subjectsInput.send_keys(Keys.DOWN)
time.sleep(1) 
subjectsInput.send_keys(Keys.DOWN)
time.sleep(1) 
subjectsInput.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "//label[normalize-space()='Reading']").click()
driver.find_element(By.XPATH, "//label[normalize-space()='Music']").click()
time.sleep(2)

driver.find_element(By.ID, "uploadPicture").send_keys("C:/Users/Z Series/Downloads/sampleFile.jpeg")
time.sleep(2)

driver.find_element(By.ID, "currentAddress").send_keys("Kota Tangerang")

driver.find_element(By.ID, "state").click()
inputState = driver.find_element(By.ID, 'react-select-3-input')
inputState.send_keys('har')
time.sleep(2)
inputState.send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element(By.ID, "city").click()
driver.find_element(By.ID, 'react-select-4-input').send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, "submit").click()

time.sleep(2)

modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
)
time.sleep(2)

modal.find_element(By.ID, "closeLargeModal").click()

time.sleep(5)