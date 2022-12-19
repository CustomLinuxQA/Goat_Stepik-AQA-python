import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from os import getenv

load_dotenv()
AUTH_EMAIL = getenv('AUTH__EMAIL')
AUTH_PASSWORD = getenv('AUTH__PASSWORD')


def test_login_form(browser):
    browser.get("https://stepik.org/lesson/236895/step/1")
    browser.implicitly_wait(15)  # Stepik иногда очень долго открывается.
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys(AUTH_EMAIL)
    browser.find_element(By.ID, "id_login_password").send_keys(AUTH_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()


