from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time, pyautogui

driver = webdriver.Chrome()
driver.get("http://demoqa.com/dragabble")
driver.maximize_window()

AC = ActionChains(driver)

# Simple drag
AC.click_and_hold(driver.find_element(By.ID, "dragBox")).move_by_offset(70, 0).release().perform()
time.sleep(2)
AC.click_and_hold(driver.find_element(By.ID, "dragBox")).move_by_offset(-70, 30).release().perform()
time.sleep(2)

# Axis Restricted drag
driver.find_element(By.ID, 'draggableExample-tab-axisRestriction').click()
time.sleep(2)

AC.click_and_hold(driver.find_element(By.ID, "restrictedX")).move_by_offset(50, 0).release().perform()
time.sleep(2)
AC.click_and_hold(driver.find_element(By.ID, "restrictedY")).move_by_offset(0, 50).release().perform()
time.sleep(2)

# Container Restricted drag
driver.find_element(By.ID, 'draggableExample-tab-containerRestriction').click()
time.sleep(2)

AC.click_and_hold(driver.find_element(By.XPATH, '//*[@id="containmentWrapper"]/div')).move_by_offset(50, 50).release().perform()
time.sleep(2)

AC.click_and_hold(driver.find_element(By.XPATH, '//*[@id="draggableExample-tabpane-containerRestriction"]/div[2]/span')).move_by_offset(50, 50).release().perform()
time.sleep(2)

# Cursor Style
driver.find_element(By.ID, 'draggableExample-tab-cursorStyle').click()
time.sleep(2)

def dragElement(element, x_offset, y_offset):
    location = element.location
    size = element.size
    x = location['x'] + size['width'] // 2
    y = location['y'] + size['height'] // 2
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveRel(x_offset, y_offset)
    pyautogui.mouseUp()

element = driver.find_element(By.ID, "cursorCenter")
dragElement(element, 50, 50)
time.sleep(2)
AC.click_and_hold(element).move_by_offset(50, 50).release().perform()
time.sleep(2)

element = driver.find_element(By.ID, "cursorTopLeft")
dragElement(element, 70, 70)
time.sleep(2)
AC.click_and_hold(element).move_by_offset(70, 70).release().perform()
time.sleep(2)

element = driver.find_element(By.ID, "cursorBottom")
dragElement(element, 90, 90)
time.sleep(2)
AC.click_and_hold(element).move_by_offset(90, 90).release().perform()
time.sleep(2)