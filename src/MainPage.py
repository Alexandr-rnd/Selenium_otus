from selenium.webdriver.support import expected_conditions as EC
from src.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    logo = (By.CSS_SELECTOR, "#logo img.img-responsive")
    basket = (By.CSS_SELECTOR, "button.dropdown-toggle.btn-lg")
    input_place = (By.CSS_SELECTOR, "input[name='search']")
    input_button = (By.CSS_SELECTOR, ".input-group-btn .btn-lg")
    main_banner = (By.CSS_SELECTOR, "div#slideshow0")
    banner_scroll = (By.CSS_SELECTOR, ".slideshow .swiper-pager .swiper-button-prev")
    macbook_air = (By.CSS_SELECTOR, ".swiper-slide-active[data-swiper-slide-index='1']")
    iphone_6 = (By.CSS_SELECTOR, "#slideshow0 .swiper-slide-active")
    swiper_button = (By.CSS_SELECTOR, ".slideshow .swiper-button-next")

    def open_main_page(self, base_url):
        self.logger.info("Opening url: {}".format(base_url))
        return self.driver.get(base_url)

    def scroll_main_banner(self):
        self.find_and_wait(locator=MainPage.iphone_6)
        self.click_element(locator=MainPage.banner_scroll)
        assert self.find_and_wait(locator=MainPage.macbook_air)

    def logo_should_be_present(self):
        assert self.find_and_wait(locator=MainPage.logo)

    def should_be_present_input_place(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.input_place))

    def should_be_present_basket(self):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.basket))

    def should_be_present_input_button(self, time=1):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.input_button))

    def should_be_present_main_banner(self, time=1):
        assert self.wait.until(EC.visibility_of_element_located(MainPage.main_banner))
