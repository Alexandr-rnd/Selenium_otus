from src.RegPage import RegPage


def test_registration_new_users(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm_and_assert()


def test_right_column(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_right_column()


def test_checkbox_confirm(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_checkbox_confirm(browser)


def test_radiobutton_subscribe(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_radiobutton_subscribe()


def test_name_place(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_input_firstname()


def test_button_accept(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_input_continue()
