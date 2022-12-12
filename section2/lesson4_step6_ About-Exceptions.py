import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.ID, "button")
    input1.click()

finally:
    time.sleep(10)
    browser.quit()

