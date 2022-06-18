import allure
from src.ElementsObject.CurrencyElement import CurrencyElement
import pytest


@allure.link('http://192.168.31.204:8081/', 'URL использованный для проверки общего элемента')
@pytest.mark.parametrize("param", ["usd", "eur", "gbp"])
@allure.title("Тест переключения валют")
def test_change_currency(browser, base_url, param):
    element_currency = CurrencyElement(browser, base_url)
    element_currency.open_base_page(base_url)
    element_currency.open_change_сurrency_list()
    element_currency.choose_usd_currency(param)
