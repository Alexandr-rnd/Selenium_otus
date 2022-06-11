import time

from src.ProductPage import ProductPage


def test_added_product_in_cart(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.click_to_add_button()
    prod_page.check_that_product_added()


def test_present_photos(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_photos()


def test_present_button_favorite(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_button_favorite()


def test_present_add_cart(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_add_car()


def test_present_contacts(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_contacts()


def test_present_activate(browser, base_url):
    prod_page = ProductPage(browser, base_url)
    prod_page.open_product_page(base_url)
    prod_page.should_be_present_activate()
