from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium import webdriver


class BasePage:
    def __init__(self, browser, base_url, wait=3):
        self.driver = browser
        self.base_url = base_url
        self.logger = browser.logger
        self.wait = WebDriverWait(browser, wait)

    def find_and_input_text(self, locator='locator', text='text'):
        self.logger.info("Input text<<{}>> in the place <<{}>>".format(text, locator))
        element = self.wait.until(EC.visibility_of_element_located(locator))
        a = Faker()
        if text == "first_name":
            element.send_keys(a.first_name())
        elif text == "second_name":
            element.send_keys(a.first_name())
        elif text == "last_name":
            element.send_keys(a.last_name())
        elif text == "email":
            element.send_keys(a.email())
        elif text == "phone_number":
            element.send_keys(a.phone_number())
        else:
            element.send_keys(text)
        return element

    def open_base_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url))
        return self.driver.get(base_url)

    def find_and_wait(self, locator='locator'):
        self.logger.info("Check if element {} is present".format(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_and_click_element(self, locator="locator"):
        self.logger.info("Clicking element: {}".format(locator))
        return self.wait.until(EC.visibility_of_element_located(locator)).click()

    def click_element(self, locator='locator'):
        self.logger.info("Simple clicking element: {}".format(locator))
        return self.driver.find_element(*locator).click()
