import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=   Service("C:\Users\aditya.joshi_infobea\Downloads\chromedriver-win64\chromedriver-win64.exe")
driver = webdriver.Chrome(service= service_obj)


# driver = webdriver.Chrome()


time.sleep(4)