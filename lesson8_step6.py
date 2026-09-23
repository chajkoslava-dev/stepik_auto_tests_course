from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calculation(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x=browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x=x.text
    x=int(x)
    answer=browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(calculation(x))
    robotCheckbox=browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")    
    robotCheckbox.click()
    robotRadioButton=browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRadioButton)
    robotRadioButton.click()
    submit=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
