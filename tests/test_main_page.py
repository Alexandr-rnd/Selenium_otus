import time
import allure
from src.MainPage import MainPage
from src.RegPage import RegPage


@allure.title("Тест согласия на подписку о новостях")
def test_add_subscribe_to_newsletter(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.go_to_newsletter_in_footer()
    m_page.confirm_subscribe_newsletter()
    m_page.continue_subscribe_newsletter()
    m_page.should_be_allert_success()


@allure.title("Тест обавления товара в карзину из списка сравниваемых товаров")
def test_add_product_in_cart_from_compare_list(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_compare_list()
    m_page.go_to_compare_list()
    m_page.add_product_to_cart_from_compare_list()
    m_page.go_to_cart_top_icons()
    m_page.should_be_added_product()


@allure.title("Тест сравнения товаров")
def test_add_2_products_in_compare_list(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_compare_list()
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_compare_list()
    m_page.go_to_compare_list()
    m_page.should_be_2_product_in_the_compare_list()


@allure.title("Тест калькулятора общей суммы в карзине ")
def test_calculate_in_the_cart(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_cart()
    m_page.go_to_cart_top_icons()
    m_page.check_calculate_x2_price_for_product()


@allure.title("Тест добавление в карзину ")
def test_add_to_cart_some_product(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_cart()
    m_page.should_be_allert_success()


@allure.title("Тест добавление в избранное")
def test_add_to_wishlist_some_product(browser, base_url):
    reg_page = RegPage(browser, base_url)
    reg_page.open_reg_page(base_url)
    reg_page.to_fill_new_user_form()
    reg_page.press_confirm()
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.press_desktops_catalog()
    m_page.press_show_all_desktops_catalog()
    m_page.choose_someone_categories()
    m_page.add_some_product_in_wishlist()
    m_page.should_be_allert_success()


@allure.title("Тест скролл главного баннера")
def test_main_banner_scroll(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.scroll_main_banner()


@allure.title("Тест наличия элемента: logo")
def test_present_logo(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.logo_should_be_present()


@allure.title("Тест наличия элемента: basket")
def test_present_basket(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_basket()


@allure.title("Тест наличия элемента: input_place")
def test_present_input_place(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_input_place()


@allure.title("Тест наличия элемента: input_button")
def test_present_input_button(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_main_banner()


@allure.title("Тест наличия элемента: main_banner")
def test_present_main_banner(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_input_button()
