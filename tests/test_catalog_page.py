from src.CatalogPage import CatalogPage


def test_search_pc(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_input_text(driver, locator=CatalogPage.search_place, text="Canon", time=1)
    CatalogPage.wait_and_click_element(driver, locator=CatalogPage.button_search)
    CatalogPage.wait_and_click_element(driver, locator=CatalogPage.canon_find)
    CatalogPage.wait_and_click_element(driver, locator=CatalogPage.canon_find)
    assert "search=Canon" in driver.current_url


def test_present_list_group(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_wait(driver, locator=CatalogPage.group_list)


def test_present_sort(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_wait(driver, locator=CatalogPage.sort)


def test_present_sort_list(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_wait(driver, locator=CatalogPage.sort_list)


def test_present_show_list(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_wait(driver, locator=CatalogPage.show_list)


def test_present_banner(driver, base_url):
    driver.get(base_url + CatalogPage.CATALOG)
    CatalogPage.find_and_wait(driver, locator=CatalogPage.present_banner)
