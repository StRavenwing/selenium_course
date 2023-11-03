from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
#import pytest

class TestReg(unittest.TestCase):

    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
            input3.send_keys("test@email.com")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(2)
            browser.quit()

    def test_reg2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
            input3.send_keys("test@email.com")
            # Отправляем заполненную форму

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
          

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()

if __name__ == '__main__':
    unittest.main()
