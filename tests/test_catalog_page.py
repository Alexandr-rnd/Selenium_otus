from src.CatalogPage import CatalogPage


def test_search_pc(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.input_search_place()
    Catalog_page.click_button_search()
    Catalog_page.click_canon_find()
    Catalog_page.find_product_in_url()


def test_present_list_group(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_list_group()


def test_present_sort(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_sort()


def test_present_sort_list(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_sort_list()


def test_present_show_list(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_show_list()


def test_present_banner(browser, base_url):
    Catalog_page = CatalogPage(browser, base_url)
    Catalog_page.open_catalog_page(base_url)
    Catalog_page.should_be_present_banner()
