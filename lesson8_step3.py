from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:  
    #link = "https://suninjuly.github.io/selects1.html"   #можешь пробовать запускать автотест по любой из этих ссылок(там разные варианты выпадающего списка)
    link = "https://suninjuly.github.io/selects2.html"    # и автотест должен успешно справляться с любой из ссылок     
    browser = webdriver.Chrome()
    browser.get(link) 
    x=browser.find_element(By.CSS_SELECTOR, ".nowrap#num1")
    y=browser.find_element(By.CSS_SELECTOR, ".nowrap#num2")
    x=x.text
    y=y.text
    sum=int(x)+int(y)
    sum=str(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum)
    button= browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
