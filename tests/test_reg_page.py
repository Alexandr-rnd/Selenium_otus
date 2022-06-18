from src.RegPage import RegPage


def test_registration_new_users(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.to_fill_new_user_form(driver)
    RegPage.press_confirm_and_assert(driver)


def test_right_column(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.should_be_present_right_column(driver)


def test_checkbox_confirm(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.should_be_present_checkbox_confirm(driver)


def test_radiobutton_subscribe(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.should_be_present_radiobutton_subscribe(driver)


def test_name_place(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.should_be_present_input_firstname(driver)


def test_button_accept(driver, base_url):
    RegPage.open_reg_page(driver, base_url)
    RegPage.should_be_present_input_continue(driver)
