from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calculation(x):
    return math.log(abs(12*math.sin(x)))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    submit=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    confirm=browser.switch_to.alert
    confirm.accept()

    number=browser.find_element(By.CSS_SELECTOR, "span#input_value")
    number=number.text
    number=int(number)

    input=browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.send_keys(calculation(number))

    submit_final=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_final.click()

finally:
    time.sleep(15)
    browser.quit()