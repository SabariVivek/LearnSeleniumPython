# JavaScript.py
from selenium.webdriver.common.alert import Alert

from Practice.SeleniumBasics.Base import *

driver = browser_launching("https://omayo.blogspot.com")

driver.execute_script("alert('I am an alert')")
alert = Alert(driver)
alert.accept()
print("I have completed the script execution...")

close_driver(driver)
