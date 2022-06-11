import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EDGEservice
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging
import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=f"C://drivers")
    parser.addoption("--url", default=f"http://192.168.31.204:8081/")
    parser.addoption("--headless", action="store_false")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def base_url(request):
    base_url = request.config.getoption("--url")
    return base_url


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver_path = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started".format(request.node.name))

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options, executable_path=f"{driver_path}/chromedriver")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=f"{driver_path}/geckodriver")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.headless = True
        service = EDGEservice(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options, executable_path=f"{driver_path}/msedgedriver")
    else:
        raise ValueError("Not found this browser!")

    logger.info("start with browser<<{}>>".format(browser_name))

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    def fin():
        driver.quit()
        logger.info("<=== Test {} finished".format(request.node.name))

    request.addfinalizer(fin)
    driver.maximize_window()
    return driver
