from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)


