import time

from src.AdminPage import AdminPage


def test_login_admin(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_input_text(driver, AdminPage.input_users, "user")
    AdminPage.find_and_input_text(driver, AdminPage.input_password, "bitnami")
    AdminPage.wait_and_click_element(driver, AdminPage.button_aut)
    assert "user_token" in driver.current_url
    time.sleep(2)


def test_present_name_place(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_wait(driver, locator=AdminPage.input_users)


def test_present_password_place(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_wait(driver, locator=AdminPage.input_password)


def test_present_button_authorization(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_wait(driver, locator=AdminPage.button_aut)


def test_present_forget_password(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_wait(driver, locator=AdminPage.forget_password)


def test_present_opencart_footer(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_wait(driver, locator=AdminPage.footer)
