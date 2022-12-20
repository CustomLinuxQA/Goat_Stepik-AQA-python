import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button(r_browser):
    r_browser.get(link)
    r_browser.implicitly_wait(5)  # ставлю на всякий случай, если нагрузка на сервер или плохой интернет.
    button = r_browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    r_browser.implicitly_wait(5)  # ставлю на всякий случай, если нагрузка на сервер или плохой интернет.
    assert len(button) > 0, 'buttons not found'
    time.sleep(5)
