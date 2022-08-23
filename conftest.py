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
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"))
    parser.addoption("--url", default=f"http://192.168.31.205:8090/")
    parser.addoption("--headless", action="store_false")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="192.168.31.204")  
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true")


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
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")

    # создаем файл логгера и форматируем для каждого теста
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs\{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started".format(request.node.name))
    if executor == "local":
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

    else:  # Переводим запуск на Хост селеноида
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "screenResolution": "1280x720",
            "name": "Alexandr",
            "selenoid:options": {
                "enableVNC": vnc
                #     "enableVideo": videos,
                #     "enableLog": logs},
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            # 'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
        )

    logger.info("start with browser<<{}>>".format(browser_name))
    # присваеваем логгер как параметр браузеру
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    class MyListener(AbstractEventListener):  # класс для создания скриншота

        def on_exception(self, exception, driver):
            logger.error(f'Oooops i got: {exception}')
            driver.save_screenshot(f'logs/screenshots/{driver.session_id}.png')

    driver = EventFiringWebDriver(driver, MyListener())

    # финализвтор как функция с логом
    def fin():
        driver.quit()
        logger.info("<=== Test {} finished".format(request.node.name))

    request.addfinalizer(fin)
    driver.maximize_window()
    return driver
