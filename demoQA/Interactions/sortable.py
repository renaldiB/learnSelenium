from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/sortable")
driver.maximize_window()

movedElement = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[3]")
targetElement = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[1]")

ActionChains(driver).click_and_hold(movedElement).move_to_element(targetElement).release().perform()

time.sleep(3)

# Move to Grid
driver.find_element(By.ID, "demo-tab-grid").click()
time.sleep(2)

movedGridElement = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-grid']/div/div/div[3]")
targetGridElement = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-grid']/div/div/div[7]")

ActionChains(driver).click_and_hold(movedGridElement).move_to_element(targetGridElement).release().perform()

time.sleep(3)