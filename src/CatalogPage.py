import allure
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

    @allure.step
    def open_catalog_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url + CatalogPage.CATALOG))
        self.driver.get(base_url + CatalogPage.CATALOG)
        return self

    @allure.step
    def should_be_present_list_group(self):
        self.logger.info("should_be_present_list_group  <<{}>>".format(CatalogPage.group_list))
        assert self.wait.until(EC.visibility_of_element_located(CatalogPage.group_list))

    @allure.step
    def should_be_present_sort(self):
        self.logger.info("should_be_present_sort  <<{}>>".format(CatalogPage.sort_list))
        assert self.wait.until(EC.visibility_of_element_located(CatalogPage.sort))

    @allure.step
    def should_be_present_sort_list(self):
        self.logger.info("should_be_present_sort_list  <<{}>>".format(CatalogPage.sort_list))
        assert self.wait.until(EC.visibility_of_element_located(CatalogPage.sort_list))

    @allure.step
    def should_be_present_show_list(self):
        self.logger.info("should_be_present_show_list  <<{}>>".format(CatalogPage.show_list))
        assert self.wait.until(EC.visibility_of_element_located(CatalogPage.show_list))

    @allure.step
    def should_be_present_banner(self):
        self.logger.info("should_be_present_banner  <<{}>>".format(CatalogPage.present_banner))
        assert self.wait.until(EC.visibility_of_element_located(CatalogPage.present_banner))

    @allure.step
    def input_search_place(self):
        self.find_and_input_text(locator=CatalogPage.search_place, text=CatalogPage.PRODUCT)

    @allure.step
    def click_button_search(self):
        self.wait_and_click_element(CatalogPage.button_search)

    @allure.step
    def click_canon_find(self):
        self.wait_and_click_element(CatalogPage.canon_find)

    @allure.step
    def find_product_in_url(self):
        self.logger.info("check url <<{}>> is contains <<{}>>".format(self.driver.current_url, CatalogPage.PRODUCT))
        assert CatalogPage.PRODUCT in self.driver.current_url
