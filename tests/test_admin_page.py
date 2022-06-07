import pytest

from src.AdminPage import AdminPage


@pytest.mark.smoke
def test_add_and_delete_product_admin(driver, base_url):
    AdminPage.open_admin_login_page(driver, base_url)
    AdminPage.input_name_user(driver)
    AdminPage.input_password_user(driver)
    AdminPage.click_button_autorization(driver)
    AdminPage.click_to_button_catalog_tab(driver)
    AdminPage.click_to_button_product_tab(driver)
    AdminPage.click_to_button_add_new_product(driver)
    AdminPage.input_name_new_product(driver)
    AdminPage.input_discription_new_product(driver)
    AdminPage.click_to_button_add_pictures(driver)
    AdminPage.click_to_button_add_pictures_cart(driver)
    AdminPage.input_tag_new_product(driver)
    AdminPage.go_to_data_tab(driver)
    AdminPage.input_model_product(driver)
    AdminPage.save_new_product(driver)
    AdminPage.click_checkbox_new_element(driver)
    AdminPage.click_button_delete_product(driver)


def test_login_admin(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.input_name_user(driver)
    AdminPage.input_password_user(driver)
    AdminPage.click_button_autorization(driver)
    AdminPage.assert_autorization(driver)


def test_present_name_place(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.should_be_present_name_place(driver)


def test_present_password_place(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.should_be_present_password_plase(driver)


def test_present_button_authorization(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.should_be_present_button_autorisation(driver)


def test_present_forget_password(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.should_be_present_forget_password(driver)


def test_present_opencart_footer(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.should_be_present_footer(driver)
