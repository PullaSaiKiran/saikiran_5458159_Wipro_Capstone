import time

from selenium.webdriver.support.ui import (
    WebDriverWait
)

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)


class BasePage:

    def __init__(
            self,
            driver
    ):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # ==================================================
    # OPEN URL
    # ==================================================

    def open_url(
            self,
            url
    ):

        self.driver.get(
            url
        )

    # ==================================================
    # WAIT METHODS
    # ==================================================

    def wait_visible(
            self,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def wait_clickable(
            self,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(
                locator
            )
        )

    def wait_presence(
            self,
            locator,
            timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.presence_of_element_located(
                locator
            )
        )

    # ==================================================
    # CLICK ELEMENT
    # ==================================================

    def click_element(
            self,
            locator,
            retries=3
    ):

        for attempt in range(retries):

            try:

                element = self.wait_clickable(
                    locator
                )

                self.scroll_to_element(
                    locator
                )

                try:

                    element.click()

                except Exception:

                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException
            ):

                time.sleep(1)

                if attempt == retries - 1:

                    raise

    # ==================================================
    # ENTER TEXT
    # ==================================================

    def enter_text(
            self,
            locator,
            text
    ):

        element = self.wait_visible(
            locator
        )

        self.scroll_to_element(
            locator
        )

        self.driver.execute_script(
            "arguments[0].focus();",
            element
        )

        element.clear()

        try:

            element.send_keys(
                str(text)
            )

        except Exception:

            self.driver.execute_script(
                """
                arguments[0].value = arguments[1];

                arguments[0].dispatchEvent(
                    new Event(
                        'input',
                        { bubbles: true }
                    )
                );

                arguments[0].dispatchEvent(
                    new Event(
                        'change',
                        { bubbles: true }
                    )
                );
                """,
                element,
                str(text)
            )

        entered_value = element.get_attribute(
            "value"
        )

        expected_value = str(text).replace(
            " ",
            ""
        )

        actual_value = entered_value.replace(
            " ",
            ""
        )

        assert actual_value == expected_value, \
            (
                f"Expected '{expected_value}' "
                f"but got '{actual_value}'"
            )

    # ==================================================
    # GET TEXT
    # ==================================================

    def get_text(
            self,
            locator
    ):

        return self.wait_visible(
            locator
        ).text.strip()

    # ==================================================
    # CHECK DISPLAYED
    # ==================================================

    def is_displayed(
            self,
            locator,
            timeout=5
    ):

        try:

            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(
                    locator
                )
            )

            return True

        except TimeoutException:

            return False

    # ==================================================
    # JAVASCRIPT CLICK
    # ==================================================

    def js_click(
            self,
            locator
    ):

        element = self.wait_presence(
            locator
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # ==================================================
    # SCROLL TO ELEMENT
    # ==================================================

    def scroll_to_element(
            self,
            locator
    ):

        element = self.wait_presence(
            locator
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView(
                {
                    block: 'center'
                }
            );
            """,
            element
        )

        time.sleep(0.5)

    # ==================================================
    # ASSERT URL
    # ==================================================

    def assert_url_contains(
            self,
            text
    ):

        current_url = (
            self.driver.current_url.lower()
        )

        assert text.lower() in current_url, \
            (
                f"Expected '{text}' "
                f"in URL but got "
                f"'{self.driver.current_url}'"
            )