import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver service
driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element(By.XPATH, "//li[contains(@aria-label,'TATKAL')]
time.sleep(2)





