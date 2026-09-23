from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calculation(x):
    return math.log(abs(12*math.sin(x)))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    other_page_button=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    other_page_button.click()

    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)

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


