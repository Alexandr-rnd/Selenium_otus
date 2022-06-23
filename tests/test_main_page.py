import allure
from src.MainPage import MainPage

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
