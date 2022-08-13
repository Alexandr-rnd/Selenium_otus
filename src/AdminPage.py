import allure
from selenium.webdriver.common.by import By
from src.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    URL_ADMIN = "admin/"

    # variableses
    PROCESSOR = "ELBRUS 100500 cor."
    MODEL = 'KALINKA'
    USER = "user"
    PASSWORD = "bitnami"

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
