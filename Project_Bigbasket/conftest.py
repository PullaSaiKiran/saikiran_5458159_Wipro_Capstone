import os

import pytest
import allure

from selenium import webdriver

from selenium.webdriver.edge.options import (
    Options as EdgeOptions
)

from selenium.webdriver.chrome.options import (
    Options as ChromeOptions
)

from utils.config_reader import ConfigReader
from utils.logger import LogGen


logger = LogGen.loggen()


@pytest.fixture(scope="function")
def driver(request):

    browser = ConfigReader.get(
        "browser"
    ).strip().lower()

    base_url = ConfigReader.get(
        "base_url"
    ).strip()

    headless = (
        ConfigReader.get("headless")
        .strip()
        .lower() == "true"
    )

    # ==========================================
    # EDGE
    # ==========================================

    if browser == "edge":

        edge_options = EdgeOptions()

        edge_options.add_argument(
            "--start-maximized"
        )

        edge_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )

        edge_options.add_experimental_option(
            "excludeSwitches",
            ["enable-automation"]
        )

        edge_options.add_experimental_option(
            "useAutomationExtension",
            False
        )

        if headless:

            edge_options.add_argument(
                "--headless"
            )

        driver = webdriver.Edge(
            options=edge_options
        )

        driver.execute_script(
            "Object.defineProperty("
            "navigator, "
            "'webdriver', "
            "{get: () => undefined}"
            ")"
        )

    # ==========================================
    # CHROME
    # ==========================================

    elif browser == "chrome":

        chrome_options = ChromeOptions()

        chrome_options.add_argument(
            "--start-maximized"
        )

        if headless:

            chrome_options.add_argument(
                "--headless"
            )

        driver = webdriver.Chrome(
            options=chrome_options
        )

    # ==========================================
    # INVALID BROWSER
    # ==========================================

    else:

        raise Exception(
            "Browser not supported"
        )

    logger.info(
        f"Opened Browser: {browser}"
    )

    driver.get(base_url)

    logger.info(
        f"Opened URL: {base_url}"
    )

    yield driver

    # ==========================================
    # SCREENSHOT ON FAILURE
    # ==========================================

    if (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    ):

        screenshots_dir = (
            "reports/screenshots"
        )

        os.makedirs(
            screenshots_dir,
            exist_ok=True
        )

        screenshot_path = os.path.join(
            screenshots_dir,
            "failure.png"
        )

        driver.save_screenshot(
            screenshot_path
        )

        with open(
            screenshot_path,
            "rb"
        ) as file:

            allure.attach(
                file.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    logger.info(
        "Closing Browser"
    )

    driver.quit()


# ==========================================
# PYTEST HOOK
# ==========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    rep = outcome.get_result()

    setattr(
        item,
        "rep_" + rep.when,
        rep
    )

def pytest_sessionfinish(session, exitstatus):

    os.system(
        "allure generate reports/allure-results -o reports/allure-report --clean"
    )

    os.system(
        "allure open reports/allure-report"
    )