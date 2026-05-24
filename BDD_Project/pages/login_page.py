from selenium.webdriver.support import (
    expected_conditions as EC
)

from pages.base_page import BasePage

from locators.login_locators import (
    LoginLocators
)


class LoginPage(BasePage):

    # ==========================================
    # OPEN BIGBASKET
    # ==========================================

    def open_bigbasket(self):

        self.open_url(
            "https://www.bigbasket.com/"
        )

    # ==========================================
    # CLICK LOGIN
    # ==========================================

    def click_login(self):

        self.click_element(
            LoginLocators.LOGIN_BUTTON
        )

    # ==========================================
    # ENTER MOBILE NUMBER
    # ==========================================

    def enter_mobile_email(
            self,
            mobile
    ):

        self.enter_text(
            LoginLocators.MOBILE_INPUT,
            mobile
        )

    # ==========================================
    # CLICK CONTINUE
    # ==========================================

    def click_continue(self):

        self.click_element(
            LoginLocators.CONTINUE_BUTTON
        )

    # ==========================================
    # CLICK VERIFY
    # ==========================================

    def click_verify_continue(self):

        self.click_element(
            LoginLocators.VERIFY_BUTTON
        )



    # ==========================================
    # INVALID MOBILE POPUP
    # ==========================================

    def get_invalid_mobile_popup(self):

        return self.wait.until(
            EC.presence_of_element_located(
                LoginLocators.INVALID_MOBILE_POPUP
            )
        )

    # ==========================================
    # INVALID OTP POPUP
    # ==========================================

    def get_invalid_otp_popup(self):

        return self.wait.until(
            EC.presence_of_element_located(
                LoginLocators.INVALID_OTP_POPUP
            )
        )