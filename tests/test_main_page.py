from src.MainPage import MainPage


def test_main_banner_scroll(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.scroll_main_banner(driver)


def test_present_logo(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.logo_should_be_present(driver)


def test_present_basket(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.should_be_present_basket(driver)


def test_present_input_place(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.should_be_present_input_place(driver)


def test_present_input_button(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.should_be_present_main_banner(driver)


def test_present_main_banner(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.should_be_present_input_button(driver)
