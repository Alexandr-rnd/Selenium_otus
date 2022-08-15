import time

import allure

from src.ProductPage import ProductPage


@allure.title("Тест добавление продукта в карзину")
def test_added_product_in_cart(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.click_to_add_button()
    prod_page.check_that_product_added()


@allure.title("Тест наличия элемента: photos")
def test_present_photos(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_photos()


@allure.title("Тест наличия элемента: button_favorite")
def test_present_button_favorite(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_button_favorite()


@allure.title("Тест наличия элемента: add_cart")
def test_present_add_cart(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_add_car()


@allure.title("Тест наличия элемента: contacts")
def test_present_contacts(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)


@allure.title("Тест наличия элемента: activate")
def test_present_activate(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_activate()
