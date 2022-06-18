from selenium.webdriver.common.by import By
from src.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
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

    def open_admin_login_page(self, base_url):
        self.get(base_url + AdminPage.URL_ADMIN)
        return self

    def click_to_button_catalog_tab(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.OPEN_CATALOG_TAB)

    def click_to_button_product_tab(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.OPEN_PRODUCT_CATALOG, time=2)

    def click_to_button_add_new_product(self):
        AdminPage.wait_and_click_element(self, AdminPage.ADD_NEW_PRODUCT_BUTTON)

    def input_name_new_product(self):
        element = AdminPage.find_and_wait(self, AdminPage.INPUT_PLACE_PRODUCT_NAME)
        element.send_keys(AdminPage.PROCESSOR)

    def input_discription_new_product(self):
        element = WebDriverWait(self, 6).until(EC.element_to_be_clickable(AdminPage.INPUT_PLACE_PRODUCT_DESCRIPTION))
        element.send_keys(AdminPage.PROCESSOR)

    def click_to_button_add_pictures(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.BUTTON_ADD_PICTURE)

    def click_to_button_add_pictures_cart(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.BUTTON_ADD_PICTURE_CART, time=3)

    def input_tag_new_product(self):
        element = WebDriverWait(self, 6).until(EC.element_to_be_clickable(AdminPage.INPUT_TAG_NAME))
        element.send_keys(AdminPage.PROCESSOR)

    def go_to_data_tab(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.BUTTON_DATA_SUBTUB)

    def input_model_product(self):
        element = WebDriverWait(self, 6).until(EC.element_to_be_clickable(AdminPage.INPUT_MODEL_DATA))
        element.send_keys(AdminPage.MODEL)

    def save_new_product(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.SAVE_CREATE_NEW_PRODUCT)

    def click_checkbox_new_element(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.DELETE_NEW_PRODUCT, time=1)

    def click_button_delete_product(self):
        AdminPage.wait_and_click_element(self, locator=AdminPage.BUTTON_DELETE_PRODUCT, time=1)
        alert = self.switch_to.alert
        alert.accept()
        alert_del = AdminPage.find_and_wait(self, locator=AdminPage.DELETE_ALERT)
        assert "You have modified products!" in alert_del.text

    def should_be_present_footer(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.footer))

    def should_be_present_forget_password(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.forget_password))

    def should_be_present_button_autorisation(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.button_aut))

    def should_be_present_password_plase(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.input_password))

    def should_be_present_name_place(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.input_users))

    def input_name_user(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.input_users))
        element.send_keys(AdminPage.USER)

    def input_password_user(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.input_password))
        element.send_keys(AdminPage.PASSWORD)

    def click_button_autorization(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(AdminPage.button_aut))
        element.click()

    def assert_autorization(self):
        assert "user_token" in self.current_url
