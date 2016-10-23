import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

driver.get('http://www.google.com')

search = driver.find_element_by_name("q")
search.send_keys("Selenium is awesome!")
search.submit()
time.sleep(10)