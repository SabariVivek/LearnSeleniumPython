# AlertHandling.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# Handling JavaScript Alerts...
basic_alert = driver.find_element(By.XPATH, "//button[contains(text(),'Alert')]")
confirm_alert = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]")
prompt_alert = driver.find_element(By.XPATH, "//button[contains(text(),'Prompt')]")

# Switching to an alert...
basic_alert.click()
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()

confirm_alert.click()
alert = driver.switch_to.alert
time.sleep(2)
alert.dismiss()

prompt_alert.click()
alert = driver.switch_to.alert
alert.send_keys("Hello Sabari")
time.sleep(2)
alert.accept()
