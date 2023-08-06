# Frames.py
from selenium.webdriver.common.by import By

from Practice.SeleniumBasics.Base import browser_launching, close_driver

driver = browser_launching("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
text = driver.find_element(By.XPATH, "//body[@id='tinymce']/p").text
print(text)

driver.switch_to.default_content()
driver.find_element(By.XPATH, "//button[@role='menuitem']/span[text()='File']").click()

close_driver(driver)
