from src.ElementsObject.CurrencyElement import CurrencyElement
import pytest


@pytest.mark.parametrize("param", ["usd", "eur", "gbp"])
def test_change_currency(browser, base_url, param):
    element_currency = CurrencyElement(browser, base_url)
    element_currency.open_base_page(base_url)
    element_currency.open_change_сurrency_list()
    element_currency.choose_usd_currency(param)
