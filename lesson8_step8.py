from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name=browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    name.send_keys("Ivanov")
    surname=browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    surname.send_keys("Ivan")
    eamil=browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    eamil.send_keys("ivanov@gmail.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'text.txt')    
    element=browser.find_element(By.CSS_SELECTOR, "input[id='file']")       
    element.send_keys(file_path)    
    submit=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
     # успеваем скопировать код за 30 секунд
    time.sleep(15)
        # закрываем браузер после всех манипуляций
    browser.quit()


   

