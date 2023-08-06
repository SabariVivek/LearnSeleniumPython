# Actions.py
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Practice.SeleniumBasics.Base import *

# driver = browser_launching("http://omayo.blogspot.com")
driver = browser_launching("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")

action = ActionChains(driver)

""" web_element_1 = driver.find_element(By.CLASS_NAME, "has-sub")
web_element_2 = driver.find_element(By.XPATH, "//*[text()='Selenium143']")
action.move_to_element(web_element_1).click(web_element_2).perform() """\

web_element_3 = driver.find_element(By.ID, "box7")
web_element_4 = driver.find_element(By.XPATH, "//*[@class='dragableBoxRight' and text()='Italy']")
action.click_and_hold(web_element_3).move_to_element(web_element_4).release().perform()

close_driver(driver)
