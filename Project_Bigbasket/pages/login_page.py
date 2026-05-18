from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login/ Sign Up')]")

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[text()='Continue']"
    )

    OTP_TEXT = (
        By.XPATH,
        "//h2[contains(text(),'Enter OTP')]"
    )
    VERIFY_BUTTON = (By.XPATH, "//button[text()='Verify & Continue']")


    def __init__(self, driver):
        super().__init__(driver)

    # Open BigBasket Website
    def open_bigbasket(self):
        self.open_url("https://www.bigbasket.com/")

    # Click Login Button
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    # Enter Mobile Number or Email
    def enter_mobile_email(self, value):
        self.enter_text(self.MOBILE_INPUT, value)

    # Click Continue
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    # Verify OTP Page
    def verify_otp_page(self):
        return self.is_displayed(self.OTP_TEXT)

    def click_verify_continue(self):
        self.click_element(self.VERIFY_BUTTON)