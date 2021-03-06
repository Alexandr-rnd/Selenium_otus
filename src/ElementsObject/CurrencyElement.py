from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class CurrencyElement(BasePage):
    CURRENCY_LIST = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY_EUR = (By.CSS_SELECTOR, "button[name = 'EUR']")
    CURRENCY_USD = (By.CSS_SELECTOR, "button[name = 'USD']")
    CURRENCY_GBP = (By.CSS_SELECTOR, "button[name = 'GBP']")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart-total")

    def open_change_сurrency_list(self):
        self.wait_and_click_element(locator=CurrencyElement.CURRENCY_LIST)

    def choose_usd_currency(self, cur):
        if cur == "usd":
            self.wait_and_click_element(locator=CurrencyElement.CURRENCY_USD)
            element = self.find_and_wait(locator=CurrencyElement.CART_BUTTON)
            assert "$" in element.text
        elif cur == "gbp":
            BasePage.wait_and_click_element(self, locator=CurrencyElement.CURRENCY_GBP)
            element = self.find_and_wait(locator=CurrencyElement.CART_BUTTON)
            assert "£" in element.text
        elif cur == "eur":
            BasePage.wait_and_click_element(self, locator=CurrencyElement.CURRENCY_EUR)
            element = self.find_and_wait(locator=CurrencyElement.CART_BUTTON)
            assert "€" in element.text
