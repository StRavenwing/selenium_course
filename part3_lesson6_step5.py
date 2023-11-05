import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestAnswer:
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1",])
    def test_pop_up(self, browser, link):
       # link = 'link'
        browser.get(link)
        browser.implicitly_wait(10)
        button = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
        button.click()

        field1 = browser.find_element(By.ID,"id_login_email")
        field1.send_keys("my_email")
        field2 = browser.find_element(By.ID, "id_login_password")
        field2.send_keys("my_password")
        button_login = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        button_login.click()

        browser.find_element(By.CLASS_NAME, "navbar__profile-img")
        browser.implicitly_wait(10)

        try:
            again = browser.find_element(By.CSS_SELECTOR, ".again-btn.white")
            again.click()
        except NoSuchElementException:
            pass

        # textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        textarea = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
        
        if textarea.text:
            textarea.clear()
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)
        
        button_send = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        # button_send = browser.find_element(By.CLASS_NAME, "submit-submission") 
        button_send.click()

        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert message.text == "Correct!", f"got: {message}"



