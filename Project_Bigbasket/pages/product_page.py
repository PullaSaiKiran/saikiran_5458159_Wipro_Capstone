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
