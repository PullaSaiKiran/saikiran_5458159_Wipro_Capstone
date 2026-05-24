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
    ghee_header = (
        By.XPATH,
        "//h1[contains(text(),'Ghee')]"
    )

    ghee_vanaspati = (
        By.XPATH,
        "//span[contains(text(),'Ghee & Vanaspati')]"
    )

    product_brands = (
        By.XPATH,
        "//h3"
    )

    added_to_basket = (
        By.XPATH,
        "//span[contains(text(),'Added')]"
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

    # ==================================================
    # GHEE ASSERT METHODS
    # SELENIUM WITH PYTEST
    # ==================================================

    def ghee_page_displayed(self):

        return self.driver.find_element(
            *self.ghee_header
        ).is_displayed()

    def ghee_category_displayed(self):

        return self.driver.find_element(
            *self.ghee_vanaspati
        ).is_displayed()

    def brand_filter_applied(
            self,
            brand_name
    ):

        products = self.driver.find_elements(
            *self.product_brands
        )

        for product in products:

            if (
                    brand_name.lower()
                    in
                    product.text.lower()
            ):
                return True

        return False

    def product_added_successfully(self):

        return self.driver.find_element(
            *self.added_to_basket
        ).is_displayed()