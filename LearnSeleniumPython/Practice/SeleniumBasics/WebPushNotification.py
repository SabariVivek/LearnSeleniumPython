# WebPushNotification.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.homedepot.com/")

time.sleep(2)
driver.close()
