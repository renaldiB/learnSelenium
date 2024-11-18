from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/selectable")

for i in range(1, 5):
    list1 = driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li['+str(i)+']')
    list1.click()
    time.sleep(1)

unselectList1 = driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[1]')
unselectList1.click()

time.sleep(3)

# Move to Grid
driver.find_element(By.ID, "demo-tab-grid").click()
time.sleep(2)

select1 = driver.find_element(By.XPATH, '//*[@id="row1"]/li[1]')
select1.click()
time.sleep(1)

select5 = driver.find_element(By.XPATH, '//*[@id="row2"]/li[2]')
select5.click()
time.sleep(1)

select9 = driver.find_element(By.XPATH, '//*[@id="row3"]/li[3]')
select9.click()
time.sleep(3)