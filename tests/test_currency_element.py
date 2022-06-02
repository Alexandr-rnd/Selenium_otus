from src.ElementsObject.CurrencyElement import CurrencyElement
import pytest


@pytest.mark.parametrize("param", ["usd", "eur", "gbp"])
def test_change_currency(driver, base_url, param):
    CurrencyElement.open_base_page(driver, base_url)
    CurrencyElement.open_change_сurrency_list(driver)
    CurrencyElement.choose_usd_currency(driver, param)
