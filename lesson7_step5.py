from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    input=browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)
    checkB = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkB.click()
    radioB = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radioB.click()
    button= browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()




