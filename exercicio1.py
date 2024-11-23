from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://google.com")
search = driver.find_element("name", "q")
search.send_keys("Python Testing with Selenium")
search.submit()
sleep(10)
driver.quit()