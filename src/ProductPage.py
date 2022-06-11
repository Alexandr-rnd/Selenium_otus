import time
from selenium.webdriver.support import expected_conditions as EC
from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # URL
    PRODUCT = "desktops/ipod-classic"

    # LOCATORS
    photos_product = (By.CSS_SELECTOR, "ul.thumbnails")
    add_button_to_favorite = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    add_button_to_cart = (By.CSS_SELECTOR, "#button-cart")
    contacts_link = (By.CSS_SELECTOR, "a [class ='atc_s addthis_button_compact']")
    list_activate = (By.CSS_SELECTOR, "li.active a")
    all_price = (By.CSS_SELECTOR, "#cart-total")

    def open_product_page(self, base_url):
        return self.driver.get(base_url + ProductPage.PRODUCT)

    def click_to_add_button(self):
        self.wait_and_click_element(locator=ProductPage.add_button_to_cart)
        time.sleep(1)

    def check_that_product_added(self):
        product = self.find_and_wait(locator=ProductPage.all_price)
        assert "1 item(s)" in product.text

    def should_be_present_photos(self):
        assert self.wait.until(EC.visibility_of_element_located(ProductPage.photos_product))

    def should_be_present_button_favorite(self):
        assert self.wait.until(EC.visibility_of_element_located(ProductPage.add_button_to_favorite))

    def should_be_present_add_car(self):
        assert self.wait.until(EC.visibility_of_element_located(ProductPage.add_button_to_cart))

    def should_be_present_contacts(self):
        assert self.wait.until(EC.visibility_of_element_located(ProductPage.contacts_link))

    def should_be_present_activate(self):
        assert self.wait.until(EC.visibility_of_element_located(ProductPage.list_activate))
