import time

import allure
from src.AdminPage import AdminPage


@allure.title("Тест добавления баннера")
def test_add_new_banner(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.go_to_disign_tab()
    adm_page.go_to_banner_tab()
    adm_page.add_new_banner()
    adm_page.input_banner_name()
    adm_page.add_banner_on_page_banners()
    adm_page.choose_some_picture_for_banner()
    adm_page.edit_picture_banner()
    adm_page.confirm_picture_bunner()
    adm_page.input_banner_title()
    adm_page.confirm_create_banner()
    adm_page.should_be_allert_success()


@allure.title("Тест фильтра по наименованию продукта")
def test_chenge_customers(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.open_customers_catalog()
    adm_page.open_customers_list()
    adm_page.create_new_customers()
    adm_page.input_customers_name()
    adm_page.input_customers_surename()
    adm_page.input_customers_email()
    adm_page.input_customers_phone_number()
    adm_page.input_customers_password()
    adm_page.save_customers_chenge()
    adm_page.input_search_customers_surename()
    adm_page.find_customers()
    adm_page.customers_edit_click()
    adm_page.select_status_customer(value="0")
    adm_page.save_edit_customer()
    adm_page.select_status_customer(value="0")
    adm_page.find_customers()
    adm_page.should_be_only_one_element()
    adm_page.customers_checkbox_click()
    adm_page.customers_danger_click()
    adm_page.close_allert()


@allure.title("Тест добавления и удаления продукта")
def test_add_and_delete_product(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.click_to_button_catalog_tab()
    adm_page.click_to_button_product_tab()
    adm_page.click_to_button_add_new_product()
    adm_page.input_name_new_product()
    adm_page.input_discription_new_product()
    adm_page.click_to_button_add_pictures()
    adm_page.click_to_button_add_pictures_cart()
    adm_page.input_tag_new_product()
    adm_page.go_to_data_tab()
    adm_page.input_model_product()
    adm_page.save_new_product()
    adm_page.click_checkbox_new_element()
    adm_page.click_button_delete_product()


@allure.title("Тест фильтра по наименованию продукта")
def test_filter_to_name_product(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.click_to_button_catalog_tab()
    adm_page.click_to_button_product_tab()
    adm_page.input_product_name_filter()
    adm_page.click_to_button_filtre()
    adm_page.should_be_only_one_element()


@allure.title("Тест изменения статуса продукта")
def test_chenge_product_status(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.click_to_button_catalog_tab()
    adm_page.click_to_button_product_tab()
    adm_page.input_product_name_filter()
    adm_page.click_to_button_filtre()
    adm_page.click_to_button_edit_product()
    adm_page.go_to_data_tab()
    adm_page.select_status_product('0')
    adm_page.click_to_button_save_edit()
    adm_page.click_to_button_filtre()
    adm_page.click_to_button_edit_product()
    adm_page.go_to_data_tab()
    adm_page.select_status_product('1')
    adm_page.click_to_button_save_edit()
    adm_page.click_to_button_filtre()
    adm_page.should_be_chenged_status_product()


@allure.title("Тест создвния пользователя")
def test_create_new_customers(browser, base_url):
    adm_page = AdminPage(browser, base_url)
    adm_page.open_admin_login_page(base_url)
    adm_page.input_password_user()
    adm_page.input_name_user()
    adm_page.click_button_autorization()
    adm_page.open_customers_catalog()
    adm_page.open_customers_list()
    adm_page.create_new_customers()
    adm_page.input_customers_name()
    adm_page.input_customers_surename()
    adm_page.input_customers_email()
    adm_page.input_customers_phone_number()
    adm_page.input_customers_password()
    adm_page.save_customers_chenge()
    adm_page.input_search_customers_surename()
    adm_page.find_customers()
    adm_page.customers_checkbox_click()
    adm_page.customers_danger_click()
    adm_page.close_allert()


@allure.title("Тест логина в админку")
def test_login_admin(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.input_name_user()
    page.input_password_user()
    page.click_button_autorization()
    page.assert_autorization()


@allure.title("Тест наличия кнопки авторизации")
def test_present_button_authorization(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_button_autorisation()


@allure.title("Тест наличия поля для имени")
def test_present_name_place(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_name_place()


@allure.title("Тест наличия поля для пароля")
def test_present_password_place(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_password_plase()


@allure.title("Тест наличия кнопки **забыл пароль**")
def test_present_forget_password(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_forget_password()


@allure.title("Тест наличия футера")
def test_present_footer(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_footer()
