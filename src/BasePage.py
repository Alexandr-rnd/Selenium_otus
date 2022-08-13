import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class BasePage:
    def __init__(self, browser, base_url, wait=3):
        self.driver = browser
        self.base_url = base_url
        self.logger = browser.logger
        self.wait = WebDriverWait(browser, wait)

    @allure.step('Ожидать, что  поле для ввода {locator} доступно и ввести текст {text}')
    def find_and_input_text(self, locator='locator', text='text'):
        self.logger.info("Input text<<{}>> in the place <<{}>>".format(text, locator))
        element = self.wait.until(EC.visibility_of_element_located(locator))
        a = Faker()
        if text == "first_name":
            var = a.first_name()
            with allure.step(title=f"{var}"):
                element.send_keys(var)
        elif text == "second_name":
            var = a.first_name()
            with allure.step(title=f"{var}"):
                element.send_keys(var)
        elif text == "last_name":
            var = a.last_name()
            with allure.step(title=f"{var}"):
                element.send_keys(var)
        elif text == "email":
            var = a.email()
            with allure.step(title=f"{var}"):
                element.send_keys(var)
        elif text == "phone_number":
            var = a.phone_number()
            with allure.step(title=f"{var}"):
                element.send_keys(var)
        else:
            element.send_keys(text)
        return element

    @allure.step('Открыть базовую страницу с url {base_url}')
    def open_base_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url))
        return self.driver.get(base_url)

    @allure.step('Ожидать, что  элемент {locator} доступен для нажатия')
    def find_and_wait(self, locator='locator'):
        self.logger.info("Check if element {} is present".format(locator))
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидать, что  элемент {locator} доступен для нажатия и сделать клик по элементу')
    def wait_and_click_element(self, locator="locator"):
        self.logger.info("Clicking element: {}".format(locator))
        return self.wait.until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Найти элемент {locator} и сделать клик по нему')
    def click_element(self, locator='locator'):
        self.logger.info("Simple clicking element: {}".format(locator))
        return self.driver.find_element(*locator).click()
