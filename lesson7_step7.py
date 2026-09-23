from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x=element.get_attribute("valuex")
    result=calc(x)
    input=browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(result)
    checkB = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkB.click()
    radioB = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radioB.click()
    button= browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()