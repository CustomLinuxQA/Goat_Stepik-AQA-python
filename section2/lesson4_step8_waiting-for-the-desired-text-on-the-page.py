from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    option1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button1 =  browser.find_element(By.ID, "book").click()

    # browser.execute_script("window.scrollBy(0, 100);", "return arguments[0].scrollIntoView(true);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()