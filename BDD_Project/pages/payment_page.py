from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from locators.payment_locators import (
    PaymentLocators
)


class PaymentPage(BasePage):

    # ==========================================
    # SWITCH TO PAYMENT IFRAME
    # ==========================================

    def switch_to_payment_frame(self):

        iframe = self.driver.find_element(
            By.TAG_NAME,
            "iframe"
        )

        self.driver.switch_to.frame(
            iframe
        )

    # ==========================================
    # CLICK PROCEED TO CHECKOUT
    # ==========================================

    def click_proceed_to_checkout(self):

        self.scroll_to_element(
            PaymentLocators.PROCEED_TO_CHECKOUT
        )

        self.js_click(
            PaymentLocators.PROCEED_TO_CHECKOUT
        )

    # ==========================================
    # ENTER INVALID CARD NUMBER
    # ==========================================
    # ==========================================
    # ENTER INVALID CARD NUMBER
    # ==========================================

    def enter_invalid_card_number(
            self,
            card_number
    ):
        self.switch_to_payment_frame()

        self.enter_text(
            PaymentLocators.CARD_NUMBER_INPUT,
            card_number
        )

        self.click_element(
            PaymentLocators.EXPIRY_INPUT
        )
    # ==========================================
    # VERIFY INVALID CARD ERROR
    # ==========================================

    def verify_invalid_card_error(self):

        assert self.is_displayed(
            PaymentLocators.INVALID_CARD_ERROR
        ), (
            "Invalid Card Error "
            "Not Displayed"
        )

        self.driver.switch_to.default_content()