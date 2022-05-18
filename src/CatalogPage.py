from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    # URL
    CATALOG = "desktops"

    # LOCATORS
    group_list = (By.CSS_SELECTOR, ".list-group")
    sort = (By.CSS_SELECTOR, "[for='input-sort']")
    sort_list = (By.CSS_SELECTOR, "#input-sort")
    show_list = (By.CSS_SELECTOR, ".col-md-3 .input-group-sm .form-control")
    present_banner = (By.CSS_SELECTOR, "a [alt='HP Banner']")
    search_place = (By.CSS_SELECTOR, ".input-lg")
    button_search = (By.CSS_SELECTOR, ".btn-lg.btn-default")
    canon_find = (By.CSS_SELECTOR, "[alt='Canon EOS 5D']")
