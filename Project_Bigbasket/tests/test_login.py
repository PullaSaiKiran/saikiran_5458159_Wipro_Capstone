
from pages.login_page import LoginPage
import time


def test_login(driver):

    login = LoginPage(driver)

    # Open Website
    login.open_bigbasket()

    # Click Login
    login.click_login()

    # Enter Mobile Number
    login.enter_mobile_email("9515703265")

    # Click Continue
    login.click_continue()

    time.sleep(15)

    # Click Verify & Continue
    login.click_verify_continue()

    # Verify OTP Page
    if login.verify_otp_page():
        print("OTP Page Displayed Successfully")
    else:
        print("OTP Page Not Displayed")