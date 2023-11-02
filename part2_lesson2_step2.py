from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    sum = str(int(num1.text) + int(num2.text))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()