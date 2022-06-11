import pytest
from src.AdminPage import AdminPage


@pytest.mark.smoke
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


@pytest.mark.smoke
def test_login_admin(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.input_name_user()
    page.input_password_user()
    page.click_button_autorization()
    page.assert_autorization()


def test_present_name_place(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_name_place()


def test_present_password_place(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_password_plase()


def test_present_button_authorization(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_button_autorisation()


def test_present_forget_password(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_forget_password()


def test_present_footer(browser, base_url):
    page = AdminPage(browser, base_url)
    page.open_admin_login_page(base_url)
    page.should_be_present_footer()
