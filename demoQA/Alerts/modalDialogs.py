from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/modal-dialogs")

smallModal = driver.find_element(By.ID, "showSmallModal")
smallModal.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "closeSmallModal"))
).click()

time.sleep(3)

largeModal = driver.find_element(By.ID, "showLargeModal")
largeModal.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "closeLargeModal"))
).click()

time.sleep(3)