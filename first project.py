import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# locators ID,Xpath, Cssselector,link text,classname name
driver.find_element(By.NAME, "email").send_keys("vmqaaj@yopmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS selector syntax tagname[attribute ='vaue'] -- input[name='name']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Aditya joshi")

#static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)

# Xpath Syntax //tagname[@attribute='value']--//input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH, "//label[@for='inlineRadio1']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Test1")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "The Form has been submitted successfully" in message



time.sleep(5)