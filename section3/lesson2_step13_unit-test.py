from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
import unittest
chromedriver_autoinstaller.install()


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".first_block > div input.first").send_keys("Мой ответ")
    browser.find_element(By.CSS_SELECTOR, ".first_block > div input.second").send_keys("Мой ответ")
    browser.find_element(By.CSS_SELECTOR, ".first_block > div input.third").send_keys("Мой ответ")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)

    return browser.find_element(By.TAG_NAME, "h1").text
#    assert "Congratulations! You have successfully registered!" == welcome_text_elt

    time.sleep(5)
    browser.quit()



class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


    def test_abs2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__": unittest.main()

# запуск через терминал
# python -m unittest lesson2_step13_unit-test.py

# ответ
# FAILED (errors=1)
