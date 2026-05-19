from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login/ Sign Up')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[text()='Continue']"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[text()='Verify & Continue']"
    )

    def open_bigbasket(self):
        self.open_url("https://www.bigbasket.com/")

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def enter_mobile_email(self, mobile):
        self.enter_text(self.MOBILE_INPUT, mobile)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def click_verify_continue(self):
        self.click_element(self.VERIFY_BUTTON)