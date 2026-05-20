from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    # Proceed Button

    PROCEED_BUTTON = (
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