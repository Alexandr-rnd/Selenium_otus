from src.AdminPage import AdminPage


def test_add_delete_product_admin(driver, base_url):
    driver.get(base_url + AdminPage.URL_ADMIN)
    AdminPage.find_and_input_text(driver, AdminPage.input_users, "user")
    AdminPage.find_and_input_text(driver, AdminPage.input_password, "bitnami")
    AdminPage.wait_and_click_element(driver, AdminPage.button_aut)
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
    AdminPage.find_and_input_text(driver, AdminPage.input_users, "user")
    AdminPage.find_and_input_text(driver, AdminPage.input_password, "bitnami")
    AdminPage.wait_and_click_element(driver, AdminPage.button_aut)
    assert "user_token" in driver.current_url


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
