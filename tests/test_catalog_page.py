from src.CatalogPage import CatalogPage


def test_search_pc(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.input_search_place(driver)
    CatalogPage.click_button_search(driver)
    CatalogPage.click_canon_find(driver)
    CatalogPage.find_product_in_url(driver)


def test_present_list_group(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.should_be_present_list_group(driver)


def test_present_sort(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.should_be_present_sort(driver)


def test_present_sort_list(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.should_be_present_sort_list(driver)


def test_present_show_list(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.should_be_present_show_list(driver)


def test_present_banner(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.should_be_present_banner(driver)
