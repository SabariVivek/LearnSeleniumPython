import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Practice.SeleniumBasics.ChromeClosingPrevention import dont_close_chrome

"""
Types of Locator :
        * ID
        * NAME
        * XPATH
        * CLASS_NAME
        * TAG_NAME
        * CSS_SELECTOR
        * LINK_TEXT
        * PARTIAL_LINK_TEXT
"""

driver = webdriver.Chrome(dont_close_chrome())
driver.maximize_window()
driver.get("https://omayo.blogspot.com")

# ID Locator
driver.find_element(By.ID, "ta1").send_keys("Hello, Sabari Vivek")

# Name Locator
driver.find_element(By.XPATH, "//option[@value='volvox']").click()

time.sleep(5)
driver.close()
