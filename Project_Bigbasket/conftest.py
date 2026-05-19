import pytest
from selenium import webdriver

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils.config_reader import ConfigReader
from utils.logger import LogGen


logger = LogGen.loggen()


@pytest.fixture(scope="function")
def driver():

    browser = ConfigReader.get("browser").strip().lower()

    base_url = ConfigReader.get("base_url").strip()

    headless = (
        ConfigReader.get("headless")
        .strip()
        .lower() == "true"
    )

    if browser == "edge":

        edge_options = EdgeOptions()

        edge_options.add_argument("--start-maximized")

        if headless:
            edge_options.add_argument("--headless")

        driver = webdriver.Edge(options=edge_options)

    elif browser == "chrome":

        chrome_options = ChromeOptions()

        chrome_options.add_argument("--start-maximized")

        if headless:
            chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

    else:
        raise Exception("Browser not supported")

    logger.info(f"Opened Browser: {browser}")

    driver.get(base_url)

    yield driver