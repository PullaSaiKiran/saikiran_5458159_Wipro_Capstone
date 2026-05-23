import time

from pages.base_page import BasePage

from locators.home_locators import (
    HomeLocators
)


class HomePage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    # ==================================================
    # CLICK TEA
    # ==================================================

    def click_tea(self):

        assert self.is_displayed(
            HomeLocators.TEA_MENU
        ), "Tea category not visible"

        self.scroll_to_element(
            HomeLocators.TEA_MENU
        )

        time.sleep(2)

        self.js_click(
            HomeLocators.TEA_MENU
        )

        time.sleep(5)

        assert (
            "tea"
            in self.driver.current_url.lower()
        ), (
            f"Tea page not opened. "
            f"Current URL: "
            f"{self.driver.current_url}"
        )

        print(
            "Tea Clicked Successfully"
        )

    # ==================================================
    # CLICK GHEE
    # ==================================================

    def click_ghee(self):

        assert self.is_displayed(
            HomeLocators.GHEE_CATEGORY
        ), "Ghee category not visible"

        self.scroll_to_element(
            HomeLocators.GHEE_CATEGORY
        )

        time.sleep(2)

        self.js_click(
            HomeLocators.GHEE_CATEGORY
        )

        time.sleep(5)

        assert (
            "ghee"
            in self.driver.current_url.lower()
        ), (
            f"Ghee page not opened. "
            f"Current URL: "
            f"{self.driver.current_url}"
        )

        print(
            "Ghee Clicked Successfully"
        )

    # ==================================================
    # OPEN BASKET
    # ==================================================

    def click_basket(self):

        assert self.is_displayed(
            HomeLocators.BASKET_BUTTON
        ), "Basket button not visible"

        self.scroll_to_element(
            HomeLocators.BASKET_BUTTON
        )

        time.sleep(2)

        self.js_click(
            HomeLocators.BASKET_BUTTON
        )

        time.sleep(3)

        assert (
            "basket"
            in self.driver.current_url.lower()
            or
            "checkout"
            in self.driver.current_url.lower()
        ), (
            f"Basket page not opened. "
            f"Current URL: "
            f"{self.driver.current_url}"
        )

        print(
            "Basket Opened Successfully"
        )

    # ==================================================
    # CLICK CHECKOUT
    # ==================================================

    def click_checkout(self):

        assert self.is_displayed(
            HomeLocators.CHECKOUT_BUTTON
        ), "Checkout button not visible"

        self.scroll_to_element(
            HomeLocators.CHECKOUT_BUTTON
        )

        time.sleep(2)

        self.js_click(
            HomeLocators.CHECKOUT_BUTTON
        )

        time.sleep(5)

        print(
            "Checkout Clicked Successfully"
        )