from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);", "return arguments[0].scrollIntoView(true);")
    input2 = browser.find_element(By.ID, "robotCheckbox").click()
    input3 = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.TAG_NAME, "button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()