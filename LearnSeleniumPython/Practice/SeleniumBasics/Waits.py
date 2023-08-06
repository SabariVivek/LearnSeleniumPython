# Waits.py
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Practice.SeleniumBasics.Base import browser_launching, close_driver

driver = browser_launching("https://omayo.blogspot.com")

# Implicitly Wait & Explicitly Wait...
# driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)

web_element = driver.find_element(By.CLASS_NAME, "dropbtn")
action = ActionChains(driver)
action.scroll_to_element(web_element)

web_element.click()

wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='myDropdown']/a[text()='Flipkart']")))
driver.find_element(By.XPATH, "//div[@id='myDropdown']/a[text()='Flipkart']").click()

close_driver(driver)
