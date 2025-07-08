import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name = 'Aditya'
#chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.NAME, "enter-name").send_keys('name')
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText= alert.text
print(alertText)
# assert name in alertText
alert.accept()











time.sleep(5)