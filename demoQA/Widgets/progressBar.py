from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/progress-bar')

# Click start button
driver.find_element(By.ID, 'startStopButton').click()

progressBar = WebDriverWait(driver, 60).until(
    EC.text_to_be_present_in_element_attribute((By.CLASS_NAME, 'progress-bar'), 'aria-valuenow', '100')
)
time.sleep(2)

# Click reset button
driver.find_element(By.ID, 'resetButton').click()
time.sleep(2)

driver.find_element(By.ID, 'startStopButton').click() # Click start button
time.sleep(2)
driver.find_element(By.ID, 'startStopButton').click() # Click stop button

time.sleep(5)
driver.quit()