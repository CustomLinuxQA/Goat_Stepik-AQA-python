from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[valuex]")
    x_valuex = x_element.get_attribute("valuex")
    x = x_valuex
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer").send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox").click()
    input3 = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
