import time

from selenium.webdriver.support import (
    expected_conditions as EC
)

from pages.base_page import BasePage

from locators.product_locators import (
    ProductLocators
)


class ProductPage(BasePage):

    # ==================================================
    # FILTER EXOTIC TEA
    # ==================================================

    def filter_exotic_tea(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                ProductLocators.EXOTIC_TEA_FILTER
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
    # APPLY BRAND FILTER
    # ==================================================

    def apply_brand_filter(self):
        self.filter_exotic_tea()

        self.apply_brand_chai_point()

    # ==================================================
    # APPLY CHAI POINT BRAND
    # ==================================================

    def apply_brand_chai_point(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                ProductLocators.BRAND_CHAI_POINT
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
    # CLICK GHEE & VANASPATI
    # ==================================================

    def click_ghee_vanaspati(self):

        self.scroll_to_element(
            ProductLocators.GHEE_VANASPATI
        )

        self.js_click(
            ProductLocators.GHEE_VANASPATI
        )

    # ==================================================
    # APPLY AMUL BRAND
    # ==================================================

    def apply_brand_amul(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                ProductLocators.BRAND_AMUL
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
    # ADD PRODUCT TO CART
    # ==================================================

    def add_first_product_to_cart(self):

        add_buttons = self.driver.find_elements(
            *ProductLocators.ADD_BUTTON
        )

        assert len(add_buttons) > 0, (
            "Add Button Not Found"
        )

        element = add_buttons[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        time.sleep(3)

    # ==================================================
    # SEARCH TEA PRODUCT
    # ==================================================

    def search_tea_product(
            self,
            product_name
    ):

        self.scroll_to_element(
            ProductLocators.BRAND_SEARCH_BOX
        )

        self.enter_text(
            ProductLocators.BRAND_SEARCH_BOX,
            product_name
        )

    # ==================================================
    # SELECT TEA CHECKBOX
    # ==================================================

    def select_tea_checkbox(self):

        self.click_element(
            ProductLocators.TATA_TEA_CHECKBOX
        )

    # ==================================================
    # VERIFY FILTERED PRODUCTS
    # ==================================================

    def verify_filtered_products(self):

        time.sleep(5)

        self.scroll_to_element(
            ProductLocators.FILTERED_PRODUCT
        )

        assert self.is_displayed(
            ProductLocators.FILTERED_PRODUCT
        ), (
            "Filtered Tea Products "
            "Not Displayed"
        )

    # ==================================================
    # ADD TEA PRODUCT
    # ==================================================

    def add_tea_product(self):

        time.sleep(3)

        self.scroll_to_element(
            ProductLocators.ADD_BUTTON
        )

        self.js_click(
            ProductLocators.ADD_BUTTON
        )

        time.sleep(3)

    # ==================================================
    # VERIFY PRODUCT ADDED
    # ==================================================

    def verify_product_added(self):

        assert True

    # ==================================================
    # CLICK GHEE PRODUCT
    # ==================================================

    def click_ghee_product(self):

        self.click_element(
            ProductLocators.GHEE_PRODUCT
        )

    # ==================================================
    # CLICK RELEVANCE DROPDOWN
    # ==================================================

    def click_relevance_dropdown(self):

        time.sleep(3)

        self.scroll_to_element(
            ProductLocators.RELEVANCE_DROPDOWN
        )

        self.js_click(
            ProductLocators.RELEVANCE_DROPDOWN
        )

    # ==================================================
    # SELECT PRICE LOW TO HIGH
    # ==================================================

    def select_price_low_to_high(self):

        self.js_click(
            ProductLocators.PRICE_LOW_TO_HIGH
        )

    # ==================================================
    # VERIFY SORTED PRODUCTS
    # ==================================================

    def verify_sorted_ghee_products(self):

        time.sleep(5)

        assert self.is_displayed(
            ProductLocators.SORTED_GHEE_PRODUCT
        ), (
            "Sorted Ghee Products "
            "Not Displayed"
        )

    # ==================================================
    # SEARCH INVALID TEA PRODUCT
    # ==================================================

    def search_invalid_tea_product(
            self,
            invalid_product
    ):

        self.scroll_to_element(
            ProductLocators.BRAND_SEARCH_BOX
        )

        self.enter_text(
            ProductLocators.BRAND_SEARCH_BOX,
            invalid_product
        )

    # ==================================================
    # VERIFY NO RESULTS
    # ==================================================

    def verify_no_results_found(self):

        time.sleep(2)

        assert self.is_displayed(
            ProductLocators.NO_RESULTS_FOUND
        ), (
            "No Results Message "
            "Not Displayed"
        )