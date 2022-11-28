import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_languages(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket, "Button adding to basket does not exist"
    time.sleep(5)