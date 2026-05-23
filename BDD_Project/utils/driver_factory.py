import configparser

from selenium import webdriver

from selenium.webdriver.chrome.service import (
    Service
)

from webdriver_manager.chrome import (
    ChromeDriverManager
)


class DriverFactory:

    @staticmethod
    def get_driver(config_path):

        config = configparser.ConfigParser()

        config.read(config_path)

        browser = config.get(
            "browser",
            "browser"
        )

        headless = config.getboolean(
            "browser",
            "headless"
        )

        if browser.lower() == "chrome":

            options = webdriver.ChromeOptions()

            options.add_argument(
                "--start-maximized"
            )

            options.add_argument(
                "--disable-notifications"
            )

            if headless:

                options.add_argument(
                    "--headless=new"
                )

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            implicit_wait = config.getint(
                "browser",
                "implicit_wait"
            )

            driver.implicitly_wait(
                implicit_wait
            )

            return driver

        raise Exception(
            f"Browser '{browser}' "
            f"not supported"
        )