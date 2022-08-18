import re
import time
from random import choice
import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    logo = (By.CSS_SELECTOR, "#logo img.img-responsive")
    basket = (By.CSS_SELECTOR, "button.dropdown-toggle.btn-lg")
    input_place = (By.CSS_SELECTOR, "input[name='search']")
    input_button = (By.CSS_SELECTOR, ".input-group-btn .btn-lg")
    main_banner = (By.CSS_SELECTOR, "div#slideshow0")
    banner_scroll = (By.CSS_SELECTOR, ".slideshow .swiper-pager .swiper-button-prev")
    macbook_air = (By.CSS_SELECTOR, ".swiper-slide-active[data-swiper-slide-index='1']")
    iphone_6 = (By.CSS_SELECTOR, "#slideshow0 .swiper-slide-active")
    swiper_button = (By.CSS_SELECTOR, ".slideshow .swiper-button-next")
    DSKTOPS = (By.XPATH, "//a[text()= 'Desktops']")
    SHOW_ALL_DSCTOPS = (By.XPATH, "//a[text()= 'Show All Desktops']")
    CATEGORIES_OF_PRODUCT = (By.CSS_SELECTOR, "div.list-group a")
    ADD_PRODUCT_IN_WISH_LIST = (By.CSS_SELECTOR, ".product-layout button[data-original-title='Add to Wish List']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    ADD_PRODUCT_IN_CART_FROM_ICONE = (By.CSS_SELECTOR, "div.button-group>button:first-child")
    GO_TO_CART_BUTTON_TOP_ICONS = (By.CSS_SELECTOR, "a[title='Shopping Cart']")
    GET_FULL_PRICE = (By.CSS_SELECTOR, "#cart-total")
    MULTIPLICATE_THE_PRODUCT = (By.CSS_SELECTOR, ".btn-block input.form-control")
    ADD_PRODUCT_IN_COMPARE_LIST = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    GO_TO_COMPARE_LIST = (By.XPATH, "//a[text()='product comparison']")
    NAME_OF_PRODUCT_IN_THE_COMPARE_LIST = (By.XPATH, "//td[text()='Product']/following-sibling::td")
    ADD_PRODUCT_IN_CART_FROM_COMPARE_LIST = (By.CSS_SELECTOR, "input.btn.btn-primary.btn-block")
    LIST_OF_PRODUCT_IN_CART = (By.CSS_SELECTOR, "#content tbody>tr>td.text-center")
    NEWSLETTER_SUBSCRIBE_IN_FOOTER = (By.XPATH, "//footer//a[text()='Newsletter']")
    RADIOBUTTON_SUBSCRIBE_NEWS = (By.CSS_SELECTOR, "input[name='newsletter'][value='1']")
    BUTTON_CONTUNUE_IN_SUBSCRIBE_NEWSLETTER = (By.CSS_SELECTOR, "input[value='Continue']")

    @allure.step
    def continue_subscribe_newsletter(self):
        self.wait_and_click_element(MainPage.BUTTON_CONTUNUE_IN_SUBSCRIBE_NEWSLETTER)

    @allure.step
    def confirm_subscribe_newsletter(self):
        self.wait_and_click_element(MainPage.RADIOBUTTON_SUBSCRIBE_NEWS)

    @allure.step
    def go_to_newsletter_in_footer(self):
        self.wait_and_click_element(MainPage.NEWSLETTER_SUBSCRIBE_IN_FOOTER)

    @allure.step
    def should_be_added_product(self):
        elements = self.find_and_wait_all_elements(MainPage.LIST_OF_PRODUCT_IN_CART)
        assert len(elements) == 1

    @allure.step
    def add_product_to_cart_from_compare_list(self):
        self.wait_and_click_element(MainPage.ADD_PRODUCT_IN_CART_FROM_COMPARE_LIST)

    @allure.step
    def should_be_2_product_in_the_compare_list(self):
        elements_all = self.find_and_wait_all_elements(MainPage.NAME_OF_PRODUCT_IN_THE_COMPARE_LIST)
        while len(elements_all) < 2:
            MainPage.press_desktops_catalog(self)
            MainPage.press_show_all_desktops_catalog(self)
            MainPage.choose_someone_categories(self)
            MainPage.add_some_product_in_compare_list(self)
        assert len(elements_all) >= 2

    @allure.step
    def go_to_compare_list(self):
        self.wait_and_click_element(MainPage.GO_TO_COMPARE_LIST)

    @allure.step
    def add_some_product_in_compare_list(self):
        elements = None
        while elements == None:
            try:
                elements = self.find_and_wait_all_elements(MainPage.ADD_PRODUCT_IN_COMPARE_LIST)
                (choice(elements)).click()
            except:
                MainPage.choose_someone_categories(self)
                elements = None

    def check_calculate_x2_price_for_product(self):
        element = self.find_and_wait(MainPage.GET_FULL_PRICE)
        price = element.text
        search = re.search(r'\d{1,6}\.\d\d', price)
        print(f'PRINT:{search.group()}')
        element = self.find_and_input_text(MainPage.MULTIPLICATE_THE_PRODUCT, text='2')
        element.send_keys(Keys.ENTER)
        element2 = self.find_and_wait(MainPage.GET_FULL_PRICE)
        price2 = element2.text
        search2 = re.search(r'\d{1,6}\.\d\d', price2)
        print(f'PRINT:{search2.group()}')
        assert float(search2.group()) == float(search.group()) * 2

    @allure.step
    def go_to_cart_top_icons(self):
        self.wait_and_click_element(MainPage.GO_TO_CART_BUTTON_TOP_ICONS)

    @allure.step
    def choose_someone_categories(self):
        elements = self.find_and_wait_all_elements(MainPage.CATEGORIES_OF_PRODUCT)
        (choice(elements)).click()

    @allure.step
    def add_some_product_in_cart(self):
        elements = None
        while elements == None:
            try:
                elements = self.find_and_wait_all_elements(MainPage.ADD_PRODUCT_IN_CART_FROM_ICONE)
                (choice(elements)).click()
            except:
                MainPage.choose_someone_categories(self)
                elements = None

    @allure.step
    def should_be_allert_success(self):
        assert "Success" in self.wait.until(EC.visibility_of_element_located(MainPage.ALERT_SUCCESS)).text

    @allure.step
    def add_some_product_in_wishlist(self):
        elements = None
        while elements == None:
            try:
                elements = self.find_and_wait_all_elements(MainPage.ADD_PRODUCT_IN_WISH_LIST)
                (choice(elements)).click()
            except:
                MainPage.choose_someone_categories(self)
                elements = None

    @allure.step
    def press_show_all_desktops_catalog(self):
        self.wait_and_click_element(MainPage.SHOW_ALL_DSCTOPS)

    @allure.step
    def press_desktops_catalog(self):
        self.wait_and_click_element(MainPage.DSKTOPS)

    @allure.step
    def open_main_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url))
        return self.driver.get(base_url)

    @allure.step
    def scroll_main_banner(self):
        self.find_and_wait(locator=MainPage.iphone_6)
        self.click_element(locator=MainPage.banner_scroll)
        assert self.find_and_wait(locator=MainPage.macbook_air)

    @allure.step
    def logo_should_be_present(self):
        assert self.find_and_wait(locator=MainPage.logo)

    @allure.step
    def should_be_present_input_place(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.input_place))

    @allure.step
    def should_be_present_basket(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.basket))

    @allure.step
    def should_be_present_input_button(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.input_button))

    @allure.step
    def should_be_present_main_banner(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.main_banner))
