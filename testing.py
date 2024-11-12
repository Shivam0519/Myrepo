from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.17.0.1")
time.sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys("Shivam")
time.sleep(3)
Password = driver.find_element(By.ID, "password")
Password.send_keys("Hello")
time.sleep(5)
