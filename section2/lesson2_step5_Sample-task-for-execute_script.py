from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);", "return arguments[0].scrollIntoView(true);")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
