from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")

clickFirstLink = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "simpleLink"))
)
clickFirstLink.click() # Created new tab (tab 2)
time.sleep(2)

# Move to the tab 1
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

clickSecondLink = driver.find_element(By.ID, "dynamicLink")
clickSecondLink.click() # Created new tab (tab 3)
time.sleep(2)

# Move to the tab 1
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

# Close all new tab (tab 2 & tab 3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()

# Back to tab 1
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)


# Click links to send API
createdApi = driver.find_element(By.ID, "created")
createdApi.click()
time.sleep(2)

noContentApi = driver.find_element(By.ID, "no-content")
noContentApi.click()
time.sleep(2)

movedApi = driver.find_element(By.ID, "moved")
movedApi.click()
time.sleep(2)

badRequestApi = driver.find_element(By.ID, "bad-request")
badRequestApi.click()
time.sleep(2)

unauthorizedApi = driver.find_element(By.ID, "unauthorized")
unauthorizedApi.click()
time.sleep(2)

forbiddenApi = driver.find_element(By.ID, "forbidden")
forbiddenApi.click()
time.sleep(2)

notFoundApi = driver.find_element(By.ID, "invalid-url")
notFoundApi.click()
time.sleep(5)