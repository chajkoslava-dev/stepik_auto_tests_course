from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calculation(x):
    return math.log(abs(12*math.sin(x)))



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book = browser.find_element(By.CSS_SELECTOR, "#book")
    book.click()

    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)


    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    input_value=input_value.text
    input_value=int(input_value)

    input=browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(calculation(input_value))

    submit.click()

finally:
    time.sleep(15)
    browser.quit()




