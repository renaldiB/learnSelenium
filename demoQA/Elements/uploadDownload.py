from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import pyautogui

# How to install pyautogui 👇
# open cmd (run as administrator) and type "pip install pyautogui"

driver = webdriver.Chrome()

driver.get("https://demoqa.com/upload-download")

# Click Download button
driver.find_element(By.ID, "downloadButton").click()
time.sleep(3)

# Upload file (tag is a "input")
driver.find_element(By.ID, "uploadFile").send_keys("C:/Users/Z Series/Downloads/sampleFile.jpeg")

# Or we can write the path like this too
# driver.find_element(By.ID, "uploadFile").send_keys("C:\\Users\\Z Series\\Downloads\\sampleFile.jpeg")

time.sleep(5)

############################################

# If the upload file tag is a "button"

# driver.get("https://gofile.io/uploadFiles")

# driver.find_element(By.CLASS_NAME, "filesUploadButton").click()
# time.sleep(3)

# pyautogui.write("C:\\Users\\Z Series\\Downloads\\sampleFile.jpeg")
# time.sleep(3)
# pyautogui.press("enter")

# time.sleep(5)