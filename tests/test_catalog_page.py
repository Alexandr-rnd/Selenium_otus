import allure
from src.CatalogPage import CatalogPage


@allure.title("Тест поиск продукта")
def test_search_pc(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.input_search_place()
    Catalog_page.click_button_search()
    Catalog_page.click_canon_find()


@allure.title("Тест наличия элемента: list_group")
def test_present_list_group(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_list_group()


@allure.title("Тест наличия элемента: sort")
def test_present_sort(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_sort()


@allure.title("Тест наличия элемента: sort_list")
def test_present_sort_list(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_sort_list()


@allure.title("Тест наличия элемента: show_list")
def test_present_show_list(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_show_list()


@allure.title("Тест наличия элемента: banner")
def test_present_banner(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_banner()
