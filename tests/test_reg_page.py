import pytest
from src.RegPage import RegPage


@pytest.mark.smoke
def test_registration_new_users(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.input_firstname, time=1)
    RegPage.find_and_input_text(driver, RegPage.input_firstname, "first_name")
    RegPage.find_and_input_text(driver, RegPage.input_lastname, "last_name")
    RegPage.find_and_input_text(driver, RegPage.input_email, "email")
    RegPage.find_and_input_text(driver, RegPage.input_telephone, "phone_number")
    RegPage.find_and_input_text(driver, RegPage.input_password, RegPage.password)
    RegPage.find_and_input_text(driver, RegPage.input_confirm, RegPage.password)
    RegPage.wait_and_click_element(driver, RegPage.checkbox_confirm)
    RegPage.wait_and_click_element(driver, RegPage.continue_button)
    assert "account/success" in driver.current_url


def test_right_column(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.right_column, time=1)


def test_checkbox_confirm(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.checkbox_confirm)


def test_radiobutton_subscribe(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.radiobutton_subscribe)


def test_name_place(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.input_firstname)


def test_button_accept(driver, base_url):
    driver.get(base_url + RegPage.REG_URL)
    RegPage.find_and_wait(driver, locator=RegPage.input_continue)
