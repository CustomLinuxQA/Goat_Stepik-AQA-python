import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from os import getenv
import math, time

load_dotenv()
link1 = "https://stepik.org/lesson/236895/step/1"
link2 = "https://stepik.org/lesson/236896/step/1"
link3 = "https://stepik.org/lesson/236897/step/1"
link4 = "https://stepik.org/lesson/236898/step/1"
link5 = "https://stepik.org/lesson/236899/step/1"
link6 = "https://stepik.org/lesson/236903/step/1"
link7 = "https://stepik.org/lesson/236904/step/1"
link8 = "https://stepik.org/lesson/236905/step/1"
AUTH_EMAIL = getenv('AUTH__EMAIL')
AUTH_PASSWORD = getenv('AUTH__PASSWORD')


@pytest.mark.parametrize('link', [link1, link2, link3, link4, link5, link6, link7, link8])
def test_login_form(browser, link):
    browser.get(link)
    browser.implicitly_wait(15)  # Stepik иногда очень долго открывается.
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys(AUTH_EMAIL)
    browser.find_element(By.ID, "id_login_password").send_keys(AUTH_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    time.sleep(15)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, ".string-quiz__textarea").send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    time.sleep(10)
    tusk_hint = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert "Correct!" in tusk_hint
    print(tusk_hint)
    time.sleep(10)

