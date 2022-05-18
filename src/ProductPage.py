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
