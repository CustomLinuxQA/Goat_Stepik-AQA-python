from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    sum = int(num1) + int(num2)

    option = Select(browser.find_element(By.ID, "dropdown"))
    option.select_by_value(str(sum))

    option2 = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(5)
    browser.quit()
