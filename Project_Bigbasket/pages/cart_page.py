from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    PROCEED_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed')]"
    )

    def click_proceed(self):
        self.click_element(self.PROCEED_BUTTON)