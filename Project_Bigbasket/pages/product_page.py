import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):

    # Exotic & Flavoured Tea

    EXOTIC_TEA_FILTER = (
        By.XPATH,
        "//a[@href='/pc/beverages/tea/exotic-flavoured-tea/?nc=ct-fa']"
    )

    # Brand Chai Point

    BRAND_CHAI_POINT = (
        By.XPATH,
        "//label[@for='i-ChaiPoint']"
    )

    # Add Button

    ADD_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Add')]"
    )

    LIMITED_QUANTITY_POPUP = (
        By.XPATH,
        "//*[contains(text(),'Limited quantity available')]"
    )
    INCREMENT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'increment')]"
    )

    tea_header = (
        By.XPATH,
        "//h1[contains(text(),'Tea')]"
    )

    exotic_tea = (
        By.XPATH,
        "//span[contains(text(),'Exotic Tea')]"
    )

    product_brands = (
        By.XPATH,
        "//h3"
    )

    added_to_basket = (
        By.XPATH,
        "//span[contains(text(),'Added')]"
    )
    # Filter Exotic Tea

    def filter_exotic_tea(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.EXOTIC_TEA_FILTER
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

        print("Exotic Tea Filter Applied")

    # Apply Chai Point Brand

    def apply_brand_chai_point(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.BRAND_CHAI_POINT
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

        print("Chai Point Brand Applied")

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

        # JS Click

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        print("Product Added Successfully")

    # ==================================================
    # PRODUCT ASSERT METHODS
    # SELENIUM WITH PYTEST
    # ==================================================

    def tea_page_displayed(self):

        return self.driver.find_element(
            *self.tea_header
        ).is_displayed()

    def exotic_tea_displayed(self):

        return self.driver.find_element(
            *self.exotic_tea
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