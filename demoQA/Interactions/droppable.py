from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()

# Simple drag and drop
dragElement = driver.find_element(By.ID, "draggable")
targetDrop = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(dragElement, targetDrop).perform()
time.sleep(2)

# Click "Accept"
driver.find_element(By.ID, "droppableExample-tab-accept").click()
time.sleep(2)

accDrag = driver.find_element(By.ID, "acceptable")
notAccDrag = driver.find_element(By.ID, "notAcceptable")
targetDrop = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(notAccDrag, targetDrop).perform()
time.sleep(2)

ActionChains(driver).drag_and_drop(accDrag, targetDrop).perform()
time.sleep(2)

# Click "Prevent Propogation"
driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()
time.sleep(2)

dragBox = driver.find_element(By.ID, "dragBox")
innerBox1 = driver.find_element(By.ID, "notGreedyInnerDropBox")
innerBox2  = driver.find_element(By.ID, "greedyDropBoxInner")

ActionChains(driver).click_and_hold(dragBox).move_by_offset(250, 0).release().perform()
time.sleep(2)
ActionChains(driver).drag_and_drop(dragBox, innerBox1).perform()
time.sleep(2)

ActionChains(driver).drag_and_drop(dragBox, innerBox2).perform()
time.sleep(2)
ActionChains(driver).click_and_hold(dragBox).move_by_offset(0, -100).release().perform()
time.sleep(2)

# Click "Revert Draggable"
driver.find_element(By.ID, "droppableExample-tab-revertable").click()
time.sleep(2)

revertBox = driver.find_element(By.ID, "revertable")
targetDrop = driver.find_element(By.ID, "droppable")
noRevertBox = driver.find_element(By.ID, "notRevertable")

ActionChains(driver).drag_and_drop(revertBox, targetDrop).perform()
time.sleep(2)

ActionChains(driver).drag_and_drop(noRevertBox, targetDrop).perform()
time.sleep(2)

ActionChains(driver).click_and_hold(noRevertBox).move_by_offset(-150, 0).release().perform()
time.sleep(5)