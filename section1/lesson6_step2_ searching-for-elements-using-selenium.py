from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")