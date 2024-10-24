from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://funkichain.com/bridge")

connect = driver.find_element(By.XPATH, '//p[text()="Connect Wallet"]')
connect.click()

connect_metamask = driver.find_element(By.CSS_SELECTOR, '[class*="g5kl0l0"]')
connect_metamask.click()

# Before using WebDriverWait
# get_wallet_button = driver.find_element(By.XPATH, "//div[text()='GET']")
# get_wallet_button.click()

# After using WebDriverWait
get_wallet_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='GET']"))
)
get_wallet_button.click()

# input = driver.find_element(By.NAME, 'from.token.inputValue')
# input.send_keys(0.01)

time.sleep(10)
driver.quit()
