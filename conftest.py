import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
DRIVERS = "C://drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=f"C://drivers")
    parser.addoption("--url", default=f"http://192.168.31.204:8081/")
    parser.addoption("--headless", action="store_true")

@pytest.fixture
def base_url(request):
    base_url = request.config.getoption("--url")
    return base_url


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver_path = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        browser = webdriver.Chrome(options=options, executable_path=f"{driver_path}/chromedriver")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        browser = webdriver.Firefox(options=options, executable_path=f"{driver_path}/geckodriver")
    elif browser_name == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        browser = webdriver.Opera(options=options, executable_path=f"{driver_path}/operadriver")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.headless = True
        browser = webdriver.Edge(options=options, executable_path=f"{driver_path}/msedgedriver")
    else:
        raise ValueError("Not found this browser!")
    request.addfinalizer(browser.close)
    return browser
