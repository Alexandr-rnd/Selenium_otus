from selenium.webdriver.common.by import By
from src.BasePage import BasePage


class AdminPage(BasePage):
    URL_ADMIN = "admin/"

    #lOCATORS
    input_users = (By.CSS_SELECTOR, "#input-username")
    input_password = (By.CSS_SELECTOR, "#input-password")
    button_aut = (By.CSS_SELECTOR, "button.btn-primary")
    forget_password = (By.CSS_SELECTOR, "span a[href]")
    footer = (By.CSS_SELECTOR, "footer#footer a[href]")

