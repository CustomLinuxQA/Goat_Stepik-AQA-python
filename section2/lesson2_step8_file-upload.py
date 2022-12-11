from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email").send_keys("Petrov@log.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file')           # добавляем к этому пути имя файла
    print(os.path.abspath(os.path.dirname(__file__)))
    input4 = browser.find_element(By.NAME, "file").send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


