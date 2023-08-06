# SeleniumBasics.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com")

# Storing a Web Element...
locator = "ta1"
web_element = driver.find_element(By.ID, locator)
web_element.send_keys("Hello, Sabari Vivek...")
web_element.clear()
web_element.send_keys("Hello, I am learning Python Selenium")

# Getting the WebElement Text...
db_text = driver.find_element(By.ID, "textbox1").text
print(db_text)
local_text = driver.find_element(By.ID, locator).get_attribute("value")
print(local_text)

# Getting Title & URL of the webpage...
print(driver.title)
print(driver.current_url)

# Closing the current & all browsers...
""" driver.close()
driver.quit() """

# Checking element is displayed, enabled, selected or not...
# Checking display status of hidden elements...
displayed = driver.find_element(By.ID, "cssmenu").is_displayed()
enabled = driver.find_element(By.ID, "but1").is_enabled()
selected = driver.find_element(By.ID, "checkbox1").is_selected()
print("Displayed :", displayed)
print("Enabled :", enabled)
print("Selected :", selected)

# Navigate Forward, Backward, Refresh ...
driver.find_element(By.LINK_TEXT, "compendiumdev").click()
driver.back()
driver.forward()
driver.back()
driver.refresh()

# Retrieving the HTML Source Code of the Web Page...
print(driver.page_source)

# Viewing the browser in full screen mode...
driver.fullscreen_window()

# Setting the size of the window...
driver.set_window_size(600, 600)
driver.maximize_window()

# Submit command...
# driver.find_element(By.ID, "but1").submit()

# Retrieving the HTML tag name of Web Element on Page...
tagname = driver.find_element(By.ID, locator).tag_name
print(tagname)

# Finding the size or location (or) both  of the web element...
new_element = driver.find_element(By.XPATH, "//h1[@class='title']")
print(new_element.size)
print(new_element.location)
print(new_element.rect)

# Setting page load time out for the website to open...
# driver.get("EXAMPLE_WEBSITE")
# driver.set_page_load_timeout(10)

# Setting page load time out for the website to open
web_elements = driver.find_elements(By.XPATH, "//select[@id='multiselect1']/option")
for element in web_elements:
    print(element.text)

# Dropdown Selection...
select_dropdown = driver.find_element(By.ID, "drop1")
select = Select(select_dropdown)
select.select_by_value("jkl")

# Closing the browser...
driver.close()
