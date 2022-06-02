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
        return self.get(base_url)

    def scroll_main_banner(self):
        MainPage.find_and_wait(self, locator=MainPage.iphone_6)
        MainPage.click_element(self, locator=MainPage.banner_scroll)
        assert MainPage.find_and_wait(self, locator=MainPage.macbook_air, time=1)
