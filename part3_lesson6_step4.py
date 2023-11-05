import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_pop_up(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    button.click()

    field1 = browser.find_element(By.ID,"id_login_email")
    field1.send_keys("my_mail")
    field2 = browser.find_element(By.ID, "id_login_password")
    field2.send_keys("my_password")
    time.sleep(5)
    button_login = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_login.click()

    with pytest.raises(NoSuchElementException):
        browser.find_element(By.ID, "ember92")
        pytest.fail("Не должно быть поп-апа")




