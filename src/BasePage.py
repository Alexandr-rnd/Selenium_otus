from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class BasePage:

    def find_and_wait(self, locator='locator', time=0):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(locator))
        return element

    def find_and_input_text(self, locator='locator', text='text', time=0):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(locator))
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

    def wait_and_click_element(self, locator="locator", time=0):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(locator))
        element.click()
        return element

    def click_element(self, locator='locator'):
        element = self.find_element(*locator)
        element.click()
        return element
