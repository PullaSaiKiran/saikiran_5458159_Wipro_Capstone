from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    # Proceed Button

    PROCEED_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed')]"
    )

    cart_header = (
        By.XPATH,
        "//h4[contains(text(),'My Basket')]"
    )

    cart_products = (
        By.XPATH,
        "//h3"
    )

    checkout_page = (
        By.XPATH,
        "//button[contains(text(),'Proceed')]"
    )

    # Click Proceed

    def click_proceed(self):

        self.scroll_to_element(
            self.PROCEED_BUTTON
        )

        self.js_click(
            self.PROCEED_BUTTON
        )

    # ==================================================
    # CART ASSERT METHODS
    # SELENIUM WITH PYTEST
    # ==================================================

    def cart_page_displayed(self):
        return self.driver.find_element(
            *self.cart_header
        ).is_displayed()

    def cart_has_products(self):
        products = self.driver.find_elements(
            *self.cart_products
        )

        return len(products) > 0

    def checkout_page_displayed(self):
        return self.driver.find_element(
            *self.checkout_page
        ).is_displayed()