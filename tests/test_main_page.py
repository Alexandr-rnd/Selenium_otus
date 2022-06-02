from src.MainPage import MainPage


def test_main_banner_scroll(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    MainPage.scroll_main_banner(driver)


def test_present_logo(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    assert MainPage.find_and_wait(driver, locator=MainPage.logo, time=1)


def test_present_basket(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    assert MainPage.find_and_wait(driver, locator=MainPage.basket, time=2)


def test_present_input_place(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    assert MainPage.find_and_wait(driver, locator=MainPage.input_place)


def test_present_input_button(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    assert MainPage.find_and_wait(driver, locator=MainPage.input_button)


def test_present_main_banner(driver, base_url):
    MainPage.open_main_page(driver, base_url)
    assert MainPage.find_and_wait(driver, locator=MainPage.main_banner)
