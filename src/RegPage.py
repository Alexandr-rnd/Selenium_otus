from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.BasePage import BasePage


class RegPage(BasePage):
    # URL
    REG_URL = "/index.php?route=account/register"

    password = "12345"

    # LOCATORS
    checkbox_confirm = (By.CSS_SELECTOR, "input[type='checkbox']")
    right_column = (By.CSS_SELECTOR, "#column-right")
    radiobutton_subscribe = (By.CSS_SELECTOR, ".radio-inline input[type='radio'][value='1']")
    input_firstname = (By.CSS_SELECTOR, "[name='firstname'].form-control")
    input_lastname = (By.CSS_SELECTOR, "[name='lastname'].form-control")
    input_email = (By.CSS_SELECTOR, "[name='email'].form-control")
    input_telephone = (By.CSS_SELECTOR, "[name='telephone'].form-control")
    input_continue = (By.CSS_SELECTOR, "input[value='Continue']")
    input_password = (By.CSS_SELECTOR, "[name='password'].form-control")
    input_confirm = (By.CSS_SELECTOR, "[name='confirm'].form-control")
    continue_button = (By.CSS_SELECTOR, "input[value = 'Continue']")

    def __init__(self, driver):
        self.driver = driver

    def open_reg_page(self, base_url):
        return self.get(base_url + RegPage.REG_URL)

    def to_fill_new_user_form(self):
        RegPage.find_and_wait(self, locator=RegPage.input_firstname, time=1)
        RegPage.find_and_input_text(self, RegPage.input_firstname, "first_name")
        RegPage.find_and_input_text(self, RegPage.input_lastname, "last_name")
        RegPage.find_and_input_text(self, RegPage.input_email, "email")
        RegPage.find_and_input_text(self, RegPage.input_telephone, "phone_number")
        RegPage.find_and_input_text(self, RegPage.input_password, RegPage.password)
        RegPage.find_and_input_text(self, RegPage.input_confirm, RegPage.password)

    def press_confirm_and_assert(self):
        RegPage.wait_and_click_element(self, RegPage.checkbox_confirm)
        RegPage.wait_and_click_element(self, RegPage.continue_button)
        assert "account/success" in self.current_url

    def should_be_present_right_column(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(RegPage.right_column))

    def should_be_present_checkbox_confirm(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(RegPage.checkbox_confirm))

    def should_be_present_radiobutton_subscribe(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(RegPage.radiobutton_subscribe))

    def should_be_present_input_firstname(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(RegPage.input_firstname))

    def should_be_present_input_continue(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(RegPage.input_continue))
