import time

from src.ProductPage import ProductPage


def test_added_product_in_cart(driver, base_url):
    ProductPage.open_product_page(driver, base_url)
    ProductPage.click_to_add_button(driver)
    time.sleep(1)
    ProductPage.check_that_product_added(driver)


def test_present_photos(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.should_be_present_photos(driver)


def test_present_button_favorite(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.should_be_present_button_favorite(driver)


def test_present_add_cart(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.should_be_present_add_car(driver)


def test_present_contacts(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.should_be_present_contacts(driver)


def test_present_activate(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.should_be_present_activate(driver)
