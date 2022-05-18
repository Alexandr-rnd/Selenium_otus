from selenium.webdriver.common.by import By
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
