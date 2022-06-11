import pytest
from src.MainPage import MainPage


def test_main_banner_scroll(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.scroll_main_banner()


def test_present_logo(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.logo_should_be_present()


def test_present_basket(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_basket()


def test_present_input_place(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_input_place()


def test_present_input_button(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_main_banner()


def test_present_main_banner(browser, base_url):
    m_page = MainPage(browser, base_url)
    m_page.open_main_page(base_url)
    m_page.should_be_present_input_button()
