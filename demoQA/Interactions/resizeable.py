from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/resizable')
driver.maximize_window()

restrictBox = driver.find_element(By.XPATH, '//*[@id="resizableBoxWithRestriction"]/span')
ActionChains(driver).click_and_hold(restrictBox).drag_and_drop_by_offset(restrictBox, 500, 300).perform()

time.sleep(3)

normalBox = driver.find_element(By.XPATH, '//*[@id="resizable"]/span')
ActionChains(driver).click_and_hold(normalBox).drag_and_drop_by_offset(normalBox, 200, 200).perform()

time.sleep(5)