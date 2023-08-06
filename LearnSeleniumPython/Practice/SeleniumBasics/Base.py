import time

from selenium import webdriver

from Practice.SeleniumBasics.ChromeClosingPrevention import dont_close_chrome


def browser_launching(url):
    driver = webdriver.Chrome(dont_close_chrome())
    driver.maximize_window()
    driver.get(url)
    return driver


def close_driver(driver):
    time.sleep(2)
    driver.close()
