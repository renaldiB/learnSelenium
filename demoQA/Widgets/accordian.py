from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/accordian")
driver.maximize_window()

def scroll_to_content(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)
    element.click()

card_2 = driver.find_element(By.ID, "section2Heading")
scroll_to_content(card_2)
time.sleep(2)

card_3 = driver.find_element(By.ID, "section3Heading")
scroll_to_content(card_3)
time.sleep(2)

card_1 = driver.find_element(By.ID, "section1Heading")
scroll_to_content(card_1)
time.sleep(2)

driver.quit()