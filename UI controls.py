import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break

radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio))
radio[2].click()
assert radio[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()








time.sleep(5)