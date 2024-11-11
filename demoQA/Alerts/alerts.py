from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

# Normal alert
alertButton = driver.find_element(By.ID, "alertButton")
alertButton.click()
driver.switch_to.alert.accept()

time.sleep(2)

# Timer alert
timerAlertButton = driver.find_element(By.ID, "timerAlertButton")
timerAlertButton.click()

WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)
driver.switch_to.alert.accept()

time.sleep(2)

# Confirmation alert
confirmAlertButton = driver.find_element(By.ID, "confirmButton")
confirmAlertButton.click()
driver.switch_to.alert.accept()

time.sleep(2)

confirmAlertButton.click()
driver.switch_to.alert.dismiss()

time.sleep(2)

# Prompt alert
promptButton = driver.find_element(By.ID, "promtButton")
promptButton.click()
driver.switch_to.alert.send_keys("RB")
driver.switch_to.alert.accept()

time.sleep(2)

promptButton.click()
driver.switch_to.alert.dismiss()

time.sleep(5)
