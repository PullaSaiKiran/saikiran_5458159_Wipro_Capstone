from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException
)

class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Open URL

    def open_url(self, url):

        self.driver.get(url)

    # Click Element

    def click_element(
            self,
            locator
    ):

        for i in range(3):

            try:

                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                element.click()

                break

            except StaleElementReferenceException:

                continue

            except Exception:

                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                break

    # Enter Text

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    # Check Element Displayed

    def is_displayed(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except Exception:

            return False

    # JavaScript Click

    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Scroll To Element

    def scroll_to_element(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )