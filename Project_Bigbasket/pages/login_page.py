from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):

    # Login Button

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login/ Sign Up')]"
    )

    # Mobile Number Input

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    # Continue Button

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[text()='Continue']"
    )

    # Verify & Continue Button

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[text()='Verify & Continue']"
    )

    INVALID_MOBILE_POPUP = (
        By.XPATH,
        "//*[contains(text(),'valid mobile number')]"
    )

    INVALID_OTP_POPUP = (
        By.XPATH,
        "//*[contains(text(),'Please Enter Valid OTP')]"
    )
    # Open BigBasket Website

    def open_bigbasket(self):

        self.open_url(
            "https://www.bigbasket.com/"
        )

    # Click Login

    def click_login(self):

        self.click_element(
            self.LOGIN_BUTTON
        )

    # Enter Mobile Number

    def enter_mobile_email(self, mobile):

        self.enter_text(
            self.MOBILE_INPUT,
            mobile
        )

    # Click Continue

    def click_continue(self):

        self.click_element(
            self.CONTINUE_BUTTON
        )

    # Click Verify & Continue

    def click_verify_continue(self):

        self.click_element(
            self.VERIFY_BUTTON
        )

    def get_invalid_mobile_popup(self):
        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_MOBILE_POPUP
            )
        )

    def get_invalid_otp_popup(self):
        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_OTP_POPUP
            )
        )