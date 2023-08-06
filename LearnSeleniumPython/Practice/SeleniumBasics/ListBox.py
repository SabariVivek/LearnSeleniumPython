# ListBox.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Base import *

driver = browser_launching("https://omayo.blogspot.com")

# List Box
web_element = driver.find_element(By.ID, "multiselect1")
select = Select(web_element)

select.select_by_value("volvox")
select.select_by_index(1)
select.select_by_visible_text("Hyundai")

time.sleep(4)
select.deselect_all()

close_driver(driver)
