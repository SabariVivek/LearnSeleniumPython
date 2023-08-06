# WindowHandling.py
from selenium.webdriver.common.by import By

from Practice.SeleniumBasics.Base import *

driver = browser_launching("https://omayo.blogspot.com")

parent_window = driver.current_window_handle
driver.find_element(By.ID, "selenium143").click()

all_windows = driver.window_handles

for window in all_windows:
    if window.__eq__(parent_window):
        driver.close()
    else:
        driver.switch_to.window(window)

is_displayed = driver.find_element(By.ID, "Header1_headerimg").is_displayed()
print(is_displayed)

close_driver(driver)
