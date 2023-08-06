import os

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com")

# Taking screenshot of a webpage (2 commands are there)...
# Declaration of absolute path...
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "Login.png")

driver.save_screenshot(path)
# driver.get_screenshot_as_file(path)
