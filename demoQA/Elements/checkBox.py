from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://demoqa.com/checkbox')

toggleClick = driver.find_element(By.CLASS_NAME, 'rct-collapse')
toggleClick.click()
time.sleep(2)

folderClick = driver.find_element(By.XPATH, '//*[@for="tree-node-home"]')
folderClick.click()
time.sleep(2)

expandAllClick = driver.find_element(By.CLASS_NAME, 'rct-option-expand-all')
expandAllClick.click()
time.sleep(2)

collapseAllClick = driver.find_element(By.CLASS_NAME, 'rct-option-collapse-all')
collapseAllClick.click()
time.sleep(2)

expandAllClick.click()
time.sleep(2)

folderClick.click()
time.sleep(2)

notesOptClick = driver.find_element(By.XPATH, '//label[@for="tree-node-notes"]')
notesOptClick.click()
time.sleep(2)

desktopOptClick = driver.find_element(By.XPATH, '//label[@for="tree-node-desktop"]')
desktopOptClick.click()
time.sleep(2)

workspaceOptClick = driver.find_element(By.XPATH, '//label[@for="tree-node-workspace"]')
workspaceOptClick.click()
time.sleep(2)

privateOptClick = driver.find_element(By.XPATH, '//label[@for="tree-node-private"]')
privateOptClick.click()
time.sleep(2)

wordFileOptClick = driver.find_element(By.XPATH, '//label[@for="tree-node-wordFile"]')
wordFileOptClick.click()

time.sleep(2)