import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com//client//auth//password-new")
driver.maximize_window()
# driver.find_element(By.CLASS_NAME, "forgot-password-link").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@1234")
# # driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")



time.sleep(5)