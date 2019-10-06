import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def  test_availability_add_button_to_basket(browser):
    
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    # используем явное ожидание
    # Если кнопка добавления товара не доступна, то в переменной button будет None,
    # и произойдет AssertionError
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    )
    
    assert button, "No found element"