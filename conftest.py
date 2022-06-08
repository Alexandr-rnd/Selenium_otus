import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FFservice
from selenium.webdriver.edge.service import Service as EDGEservice
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=f"C://drivers")
    parser.addoption("--url", default=f"http://192.168.31.204:8081/")
    parser.addoption("--headless", action="store_false")


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
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options, executable_path=f"{driver_path}/chromedriver")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        service = FFservice(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options, executable_path=f"{driver_path}/geckodriver")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.headless = True
        service = EDGEservice(executable_path=EdgeChromiumDriverManager().install())
        browser = webdriver.Edge(service=service, options=options, executable_path=f"{driver_path}/msedgedriver")
    else:
        raise ValueError("Not found this browser!")

    request.addfinalizer(browser.close)
    browser.maximize_window()
    return browser
