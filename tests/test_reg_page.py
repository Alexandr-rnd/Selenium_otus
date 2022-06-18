import allure

from src.RegPage import RegPage


@allure.title("Тест на регистрации нового пользователя")
def test_registration_new_users(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm_and_assert()


@allure.title("Тест наличия боковой панели")
def test_right_column(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_right_column()


@allure.title("Тест наличия элемента: button_accept")
def test_checkbox_confirm(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_checkbox_confirm(browser)


@allure.title("Тест наличия элемента: radiobutton_subscribe")
def test_radiobutton_subscribe(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_radiobutton_subscribe()


@allure.title("Тест наличия элемента: name")
def test_name_place(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_input_firstname()


@allure.title("Тест наличия элемента: button_accept")
def test_button_accept(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.should_be_present_input_continue()
