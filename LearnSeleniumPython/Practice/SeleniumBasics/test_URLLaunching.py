from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
    * After having executed the code, 
      Chrome Driver got killed because the Python app finishes its execution...
      
    * If you want the Browser opened by the Driver to stay open use Chrome option and add detach
    
    Code --> chrome_options = Options()
             chrome_options.add_experimental_option("detach", True)
"""


def test_chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    driver.close()
