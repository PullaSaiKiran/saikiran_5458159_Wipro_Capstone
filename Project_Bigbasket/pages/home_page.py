import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    # Tea Category

    TEA_MENU = (
        By.XPATH,
        "//span[text()='Tea']"
    )

    # Ghee Category

    GHEE_CATEGORY = (
        By.XPATH,
        "//a[contains(@href,'ghee')]"
    )

    # Basket Button

    BASKET_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'basket')]"
    )

    # Proceed To Checkout

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )

    def __init__(self, driver):

        super().__init__(driver)

    # Click Tea

    def click_tea(self):

        self.scroll_to_element(
            self.TEA_MENU
        )

        time.sleep(2)

        self.js_click(
            self.TEA_MENU
        )

        print("Tea Clicked Successfully")

    # Click Ghee

    def click_ghee(self):

        self.scroll_to_element(
            self.GHEE_CATEGORY
        )

        time.sleep(2)

        self.js_click(
            self.GHEE_CATEGORY
        )

        print("Ghee Clicked Successfully")

    # Open Basket

    def click_basket(self):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.BASKET_BUTTON
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

        print("Basket Opened Successfully")

    # Proceed To Checkout

    def click_checkout(self):

        self.scroll_to_element(
            self.CHECKOUT_BUTTON
        )

        time.sleep(2)

        self.js_click(
            self.CHECKOUT_BUTTON
        )

        print("Checkout Clicked Successfully")