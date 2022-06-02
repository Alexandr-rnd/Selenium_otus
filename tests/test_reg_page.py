from src.RegPage import RegPage


def test_registration_new_users(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.to_fill_new_user_form(driver)
    RegPage.press_confirm_and_assert(driver)


def test_right_column(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.find_and_wait(driver, locator=RegPage.right_column, time=1)


def test_checkbox_confirm(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.find_and_wait(driver, locator=RegPage.checkbox_confirm)


def test_radiobutton_subscribe(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.find_and_wait(driver, locator=RegPage.radiobutton_subscribe)


def test_name_place(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.find_and_wait(driver, locator=RegPage.input_firstname)


def test_button_accept(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.find_and_wait(driver, locator=RegPage.input_continue)
