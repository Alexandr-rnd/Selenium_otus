from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    # URL
    CATALOG = "desktops"
    PRODUCT = "Canon"

    # LOCATORS
    group_list = (By.CSS_SELECTOR, ".list-group")
    sort = (By.CSS_SELECTOR, "[for='input-sort']")
    sort_list = (By.CSS_SELECTOR, "#input-sort")
    show_list = (By.CSS_SELECTOR, ".col-md-3 .input-group-sm .form-control")
    present_banner = (By.CSS_SELECTOR, "a [alt='HP Banner']")
    search_place = (By.CSS_SELECTOR, ".input-lg")
    button_search = (By.CSS_SELECTOR, ".btn-lg.btn-default")
    canon_find = (By.CSS_SELECTOR, "[alt='Canon EOS 5D']")

    def should_be_present_list_group(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.group_list))

    def should_be_present_sort(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.sort))

    def should_be_present_sort_list(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.sort_list))

    def should_be_present_show_list(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.show_list))

    def should_be_present_banner(self, time=1):
        assert WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.present_banner))

    def input_search_place(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.search_place))
        element.send_keys(CatalogPage.PRODUCT)

    def click_button_search(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.button_search))
        element.click()

    def click_canon_find(self, time=1):
        element = WebDriverWait(self, time).until(EC.visibility_of_element_located(CatalogPage.canon_find))
        element.click()

    def find_product_in_url(self):
        assert CatalogPage.PRODUCT in self.current_url
