import time

from selenium import webdriver
#chrome driver service
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)









time.sleep(2)