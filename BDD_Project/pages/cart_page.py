from pages.base_page import BasePage

from locators.cart_locators import (
    CartLocators
)


class CartPage(BasePage):

    # ==================================================
    # OPEN CART
    # ==================================================

    def open_cart(self):

        assert self.is_displayed(
            CartLocators.CART_BUTTON
        ), "Cart button not visible"

        self.scroll_to_element(
            CartLocators.CART_BUTTON
        )

        self.js_click(
            CartLocators.CART_BUTTON
        )

        self.assert_url_contains(
            "basket"
        )

    # ==================================================
    # VERIFY CART HAS ITEMS
    # ==================================================

    def verify_cart_has_items(self):
        items = self.driver.find_elements(
            *CartLocators.CART_ITEMS
        )

        assert len(items) > 0, \
            "Cart is empty"

        print(
            f"Cart contains "
            f"{len(items)} item(s)"
        )
    # ==================================================
    # CLICK PROCEED
    # ==================================================

    def click_proceed(self):

        assert self.is_displayed(
            CartLocators.PROCEED_BUTTON
        ), "Proceed button not visible"

        self.scroll_to_element(
            CartLocators.PROCEED_BUTTON
        )

        self.js_click(
            CartLocators.PROCEED_BUTTON
        )

    # ==================================================
    # VERIFY CHECKOUT PAGE
    # ==================================================

    def verify_checkout_page(self):

        assert (
            self.is_displayed(
                CartLocators.CHECKOUT_PAGE
            )
            or
            "checkout"
            in self.driver.current_url.lower()
        ), "Checkout page not displayed"

    # ==========================================
    # DELETE PRODUCT
    # ==========================================

    def delete_product(self):
        import time

        time.sleep(2)

        self.scroll_to_element(
            CartLocators.DELETE_BUTTON
        )

        self.js_click(
            CartLocators.DELETE_BUTTON
        )

        print(
            "Product Deleted Successfully"
        )

    # ==========================================
    # VERIFY PRODUCT REMOVED
    # ==========================================

    def verify_product_removed(self):
        import time

        time.sleep(3)

        page_text = self.driver.page_source.lower()

        assert (
                "empty"
                in page_text
        ), (
            "Product Not Removed"
        )

        print(
            "Product Removed Successfully"
        )

    # ==================================================
    # VERIFY PRODUCT ADDED
    # ==================================================

    def verify_product_added(self):
        import time

        time.sleep(3)

        assert self.is_displayed(
            CartLocators.CART_PRODUCT
        ), (
            "Tea Product "
            "Not Added To Cart"
        )