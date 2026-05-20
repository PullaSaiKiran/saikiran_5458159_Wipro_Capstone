import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class GheePage(BasePage):

    # Ghee & Vanaspati

    GHEE_VANASPATI = (
        By.XPATH,
        "//a[normalize-space()='Ghee & Vanaspati']"
    )

    # Brand Amul

    BRAND_AMUL = (
        By.XPATH,
        "//label[@for='i-Amul']"
    )

    # Add Button

    ADD_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Add')]"
    )

    # Click Ghee & Vanaspati

    def click_ghee_vanaspati(self):

        self.scroll_to_element(
            self.GHEE_VANASPATI
        )

        self.js_click(
            self.GHEE_VANASPATI
        )

    # Apply Amul Brand Filter

    def apply_brand_amul(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.BRAND_AMUL
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Add Product To Cart

    def add_first_product_to_cart(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.ADD_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )