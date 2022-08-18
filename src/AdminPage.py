import allure
from selenium.webdriver.common.by import By
from src.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    URL_ADMIN = "admin/"
    USER = "user"
    PASSWORD = "bitnami"
    PRODUCT = "iPhone"

    # variableses
    PROCESSOR = "ELBRUS 100500 cor."
    MODEL = 'KALINKA'
    MODEL_FOR_TEST_FILTER = 'iPhone'

    # lOCATORS
    input_users = (By.CSS_SELECTOR, "#input-username")
    input_password = (By.CSS_SELECTOR, "#input-password")
    button_aut = (By.CSS_SELECTOR, "button.btn-primary")
    forget_password = (By.CSS_SELECTOR, "span a[href]")
    footer = (By.CSS_SELECTOR, "footer#footer a[href]")
    OPEN_CATALOG_TAB = (By.CSS_SELECTOR, "#menu-catalog")
    OPEN_PRODUCT_CATALOG = (By.XPATH, "//a[text()='Products']")
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    INPUT_PLACE_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_PLACE_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.note-editing-area div.note-editable")
    BUTTON_ADD_PICTURE = (By.CSS_SELECTOR, "button[aria-label='Picture']")
    BUTTON_ADD_PICTURE_CART = (By.CSS_SELECTOR, "img[title='cart.png']")
    INPUT_TAG_NAME = (By.CSS_SELECTOR, "#input-meta-title1")
    BUTTON_DATA_SUBTUB = (By.XPATH, "//a[text()='Data']")
    INPUT_MODEL_DATA = (By.CSS_SELECTOR, "#input-model")
    SAVE_CREATE_NEW_PRODUCT = (By.CSS_SELECTOR, ".pull-right button")
    DELETE_NEW_PRODUCT = (By.XPATH, f"//td[text()='{MODEL}']/preceding-sibling::td[input]")
    BUTTON_DELETE_PRODUCT = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    DELETE_ALERT = (By.CSS_SELECTOR, "div.alert")
    FIND_PRODUCT_INPUT = (By.CSS_SELECTOR, "input#input-name")
    BUTTON_FILTER = (By.CSS_SELECTOR, "button#button-filter")
    BUTTON_EDIT_PRODUCT = (By.CSS_SELECTOR, "td a.btn-primary")
    BUTTON_SELECT_STATUS = (By.CSS_SELECTOR, "select#input-status")
    BUTTON_SAVE_EDIT_PRODUCT = (By.CSS_SELECTOR, "button.btn-primary[type=submit]")
    STATUS_PRODUCT_IN_PRODUCT_LIST = (By.XPATH, "//td[text()='Enabled']")
    CUSTOMERS_CATALOG = (By.CSS_SELECTOR, "li#menu-customer")
    CUSTOMERS_CATALOG_MAIN = (By.CSS_SELECTOR, "#collapse5 li:first-child a")
    BUTTON_NEW_CUSTOMERS = (By.CSS_SELECTOR, ".pull-right a")
    NAME_CUSTOMERS = (By.CSS_SELECTOR, "#input-firstname")
    SURENAME_CUSTOMERS = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_CUSTOMERS = (By.CSS_SELECTOR, "#input-email")
    NUMBER_PHONE_CUSTOMERS = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_CUSTOMERS = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD_CUSTOMERS = (By.CSS_SELECTOR, "#input-confirm")
    BUTTON_SAVE_CUSTOMERS_CREATE_FORM = (By.CSS_SELECTOR, "button.btn-primary")
    NAME_FILTRE = (By.CSS_SELECTOR, "#input-name")
    CHECKBOX_FOR_USER = (By.CSS_SELECTOR, "thead .text-center input[type='checkbox']")
    BUTTON_FILTER_FIND_CUSTOMERS = (By.CSS_SELECTOR, "button#button-filter")
    BUTTON_DANGER = (By.CSS_SELECTOR, "button.btn-danger")
    BUTTON_EDIT_CUSTOMERS = (By.CSS_SELECTOR, "td.text-right a.btn")
    SELECT_STATUS_CUSTOMER = (By.CSS_SELECTOR, "#input-status")
    SAVE_EDIT_CUSTOMERS = (By.CSS_SELECTOR, "#content .pull-right button.btn-primary")
    CUSTOMERS_LIST = (By.CSS_SELECTOR, ".table-hover tbody")
    DESIGN_TAB = (By.CSS_SELECTOR, "#menu-design a.collapsed")
    BANNERS_TAB = (By.XPATH, "//a[text()='Banners']")
    BUTTON_ADD_NEW_BUNNER = (By.CSS_SELECTOR, "div.pull-right a")
    BANNER_NAME = (By.CSS_SELECTOR, "#input-name")
    BUTTON_ADD_BUNNER_IN_PAGE_BUNNER = (By.CSS_SELECTOR, "button[data-original-title='Add Banner']")
    BUTTON_ADD_IMAGE_BUNNER = (By.CSS_SELECTOR, "a#thumb-image0")
    BUTTON_EDIT_IMAGE_BUNNER = (By.CSS_SELECTOR, "#button-image")
    SOME_IMAGE_FOR_TEST = (By.CSS_SELECTOR, "img[alt='profile-pic.pn g']")
    BUTTON_ADD_NEW_BUNNER1 = (By.CSS_SELECTOR, "a#thumb-image1")
    BUTTON_SAVE_CONFIG_BUNNER = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    INPUT_TITLE_BANNER = (By.CSS_SELECTOR, "input[placeholder='Title']")
    ALLERT_SUCCSESSFUL = (By.CSS_SELECTOR, "div.alert-success")

    @allure.step
    def input_banner_title(self):
        self.find_and_input_text(locator=AdminPage.INPUT_TITLE_BANNER, text="title")

    @allure.step
    def confirm_create_banner(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_SAVE_CONFIG_BUNNER)

    @allure.step
    def confirm_picture_bunner(self):
        self.wait_and_click_element(locator=AdminPage.SOME_IMAGE_FOR_TEST)

    @allure.step
    def edit_picture_banner(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_EDIT_IMAGE_BUNNER)

    @allure.step
    def choose_some_picture_for_banner(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_ADD_IMAGE_BUNNER)

    @allure.step
    def add_banner_on_page_banners(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_ADD_BUNNER_IN_PAGE_BUNNER)

    @allure.step
    def input_banner_name(self):
        self.find_and_input_text(locator=AdminPage.BANNER_NAME, text="test_banner")

    @allure.step
    def add_new_banner(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_ADD_NEW_BUNNER)

    @allure.step
    def go_to_banner_tab(self):
        self.wait_and_click_element(locator=AdminPage.BANNERS_TAB)

    @allure.step
    def go_to_disign_tab(self):
        self.wait_and_click_element(locator=AdminPage.DESIGN_TAB)

    @allure.step
    def should_be_only_one_customers(self):
        elements = self.find_and_wait_all_elements(locator=AdminPage.CUSTOMERS_LIST)
        assert len(elements) == int(1)

    @allure.step
    def save_edit_customer(self):
        self.wait_and_click_element(locator=AdminPage.SAVE_EDIT_CUSTOMERS)

    @allure.step
    def select_status_customer(self, value=''):
        self.select_elemen_from_dropdown(locator=AdminPage.SELECT_STATUS_CUSTOMER, value=value)

    @allure.step
    def customers_edit_click(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_EDIT_CUSTOMERS)

    @allure.step
    def close_allert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    @allure.step
    def customers_danger_click(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_DANGER)

    @allure.step
    def customers_checkbox_click(self):
        self.wait_and_click_element(locator=AdminPage.CHECKBOX_FOR_USER)

    @allure.step
    def find_customers(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_FILTER_FIND_CUSTOMERS)

    @allure.step
    def input_search_customers_surename(self):
        self.find_and_input_text(locator=AdminPage.NAME_FILTRE, text="test_and_delete")

    @allure.step
    def save_customers_chenge(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_SAVE_CUSTOMERS_CREATE_FORM)

    @allure.step
    def input_customers_password(self):
        self.find_and_input_text(locator=AdminPage.PASSWORD_CUSTOMERS, text="1234")
        self.find_and_input_text(locator=AdminPage.CONFIRM_PASSWORD_CUSTOMERS, text="1234")

    @allure.step
    def input_customers_phone_number(self):
        self.find_and_input_text(locator=AdminPage.NUMBER_PHONE_CUSTOMERS, text="phone_number")

    @allure.step
    def input_customers_email(self):
        self.find_and_input_text(locator=AdminPage.EMAIL_CUSTOMERS, text="email")

    @allure.step
    def input_customers_surename(self):
        self.find_and_input_text(locator=AdminPage.SURENAME_CUSTOMERS, text="test_and_delete")

    @allure.step
    def input_customers_name(self):
        self.find_and_input_text(locator=AdminPage.NAME_CUSTOMERS, text="first_name")

    @allure.step
    def create_new_customers(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_NEW_CUSTOMERS)

    @allure.step
    def open_customers_catalog(self):
        self.wait_and_click_element(locator=AdminPage.CUSTOMERS_CATALOG)

    @allure.step
    def open_customers_list(self):
        self.wait_and_click_element(locator=AdminPage.CUSTOMERS_CATALOG_MAIN)

    @allure.step
    def should_be_chenged_status_product(self):
        element = self.find_and_wait(locator=AdminPage.STATUS_PRODUCT_IN_PRODUCT_LIST)
        assert element.text == "Enabled"

    @allure.step
    def click_to_button_save_edit(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_SAVE_EDIT_PRODUCT)

    @allure.step
    def select_status_product(self, value=''):
        self.select_elemen_from_dropdown(locator=AdminPage.BUTTON_SELECT_STATUS, value=value)

    @allure.step
    def click_to_button_edit_product(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_EDIT_PRODUCT)

    @allure.step
    def click_to_button_filtre(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_FILTER)

    @allure.step
    def should_be_only_one_element(self):
        elements = self.find_and_wait_all_elements(locator=AdminPage.ADD_NEW_PRODUCT_BUTTON)
        assert len(elements) == int(1)

    @allure.step
    def input_product_name_filter(self):
        self.find_and_input_text(locator=AdminPage.FIND_PRODUCT_INPUT, text=AdminPage.MODEL_FOR_TEST_FILTER)
        return self

    @allure.step
    def open_admin_login_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url + AdminPage.URL_ADMIN))
        self.driver.get(base_url + AdminPage.URL_ADMIN)
        return self

    @allure.step
    def click_to_button_catalog_tab(self):
        self.wait_and_click_element(locator=AdminPage.OPEN_CATALOG_TAB)

    @allure.step
    def click_to_button_product_tab(self):
        self.wait_and_click_element(locator=AdminPage.OPEN_PRODUCT_CATALOG)

    @allure.step
    def click_to_button_add_new_product(self):
        self.wait_and_click_element(locator=AdminPage.ADD_NEW_PRODUCT_BUTTON)

    @allure.step
    def input_name_new_product(self):
        self.find_and_input_text(AdminPage.INPUT_PLACE_PRODUCT_NAME, AdminPage.PROCESSOR)

    @allure.step
    def input_discription_new_product(self):
        self.find_and_input_text(locator=AdminPage.INPUT_PLACE_PRODUCT_DESCRIPTION, text=AdminPage.PROCESSOR)

    @allure.step
    def click_to_button_add_pictures(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_ADD_PICTURE)

    @allure.step
    def click_to_button_add_pictures_cart(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_ADD_PICTURE_CART)

    @allure.step
    def input_tag_new_product(self):
        self.find_and_input_text(locator=AdminPage.INPUT_TAG_NAME, text=AdminPage.PROCESSOR)

    @allure.step
    def go_to_data_tab(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_DATA_SUBTUB)

    @allure.step
    def input_model_product(self):
        self.find_and_input_text(locator=AdminPage.INPUT_MODEL_DATA, text=AdminPage.MODEL)

    @allure.step
    def save_new_product(self):
        self.wait_and_click_element(locator=AdminPage.SAVE_CREATE_NEW_PRODUCT)

    @allure.step
    def click_checkbox_new_element(self):
        self.wait_and_click_element(locator=AdminPage.DELETE_NEW_PRODUCT)

    @allure.step
    def click_button_delete_product(self):
        self.wait_and_click_element(locator=AdminPage.BUTTON_DELETE_PRODUCT)
        self.logger.info("switch_to alert <<{}>>".format(AdminPage.button_aut))
        alert = self.driver.switch_to.alert
        self.logger.info("switch_to alert <<{}>>".format(alert.text))
        alert.accept()
        alert_del = AdminPage.find_and_wait(self, locator=AdminPage.DELETE_ALERT)
        assert "You have modified products!" in alert_del.text

    @allure.step
    def should_be_present_footer(self):
        self.logger.info("should_be_present_footer  <<{}>>".format(AdminPage.footer))
        assert self.wait.until(EC.visibility_of_element_located(AdminPage.footer))

    @allure.step
    def should_be_present_forget_password(self):
        self.logger.info("should_be_present_forget_password  <<{}>>".format(AdminPage.forget_password))
        assert self.wait.until(EC.visibility_of_element_located(AdminPage.forget_password))

    @allure.step
    def should_be_present_button_autorisation(self):
        self.logger.info("should_be_present_button_autorisation  <<{}>>".format(AdminPage.button_aut))
        assert self.wait.until(EC.visibility_of_element_located(AdminPage.button_aut))

    @allure.step
    def should_be_present_password_plase(self):
        self.logger.info("should_be_present_password_plase  <<{}>>".format(AdminPage.input_password))
        assert self.wait.until(EC.visibility_of_element_located(AdminPage.input_password))

    @allure.step
    def should_be_present_name_place(self):
        self.logger.info("should_be_present_name_place  <<{}>>".format(AdminPage.input_users))
        assert self.wait.until(EC.visibility_of_element_located(AdminPage.input_users))

    @allure.step
    def input_name_user(self):
        self.logger.info("input_name_user <<{}>>".format(AdminPage.USER))
        self.find_and_input_text(locator=AdminPage.input_users, text=AdminPage.USER)

    @allure.step
    def input_password_user(self):
        self.find_and_input_text(locator=AdminPage.input_password, text=AdminPage.PASSWORD)

    @allure.step
    def click_button_autorization(self):
        self.logger.info("click_button_autorization to selector <<{}>>".format(AdminPage.button_aut))
        self.wait_and_click_element(locator=AdminPage.button_aut)

    @allure.step
    def assert_autorization(self):
        self.logger.info("assert_autorization URL <<{}>>".format(self.driver.current_url))
        assert "user_token" in self.driver.current_url

    @allure.step
    def should_be_allert_success(self):
        assert "Success" in self.wait.until(EC.visibility_of_element_located(AdminPage.ALLERT_SUCCSESSFUL)).text
