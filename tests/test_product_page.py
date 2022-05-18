from src.ProductPage import ProductPage


def test_added_product_in_cart(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.wait_and_click_element(driver, locator=ProductPage.add_button_to_cart)
    ProductPage.find_and_wait(driver, locator=ProductPage.add_button_to_cart)
    summ = ProductPage.find_and_wait(driver, locator=ProductPage.all_price, time=1)
    assert summ.text == "1 item(s) - $122.00"


def test_present_photos(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.find_and_wait(driver, locator=ProductPage.photos_product)


def test_present_button_favorite(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.find_and_wait(driver, locator=ProductPage.add_button_to_favorite)


def test_present_add_cart(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.find_and_wait(driver, locator=ProductPage.add_button_to_cart)


def test_present_contacts(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.find_and_wait(driver, locator=ProductPage.contacts_link)


def test_present_activate(driver, base_url):
    driver.get(base_url + ProductPage.PRODUCT)
    ProductPage.find_and_wait(driver, locator=ProductPage.list_activate)
