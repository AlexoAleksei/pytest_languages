import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_languages(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    if browser.find_element(By.CSS_SELECTOR, "[name='language'] > [value='fr']").get_attribute("selected"): #Выставлен французский язык
        print("French language selected")
        assert button_add_to_basket.text == "Ajouter au panier", "Button adding to basket has wrong text in french"
    time.sleep(30)