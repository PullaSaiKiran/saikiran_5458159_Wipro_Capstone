from behave import given, when, then

import configparser
import time

from pages.login_page import (
    LoginPage
)

from pages.home_page import (
    HomePage
)

from pages.payment_page import (
    PaymentPage
)

from pages.product_page import (
    ProductPage
)

from pages.cart_page import (
    CartPage
)

from locators.login_locators import (
    LoginLocators
)

from utils.excel_reader import (
    ExcelReader
)

from utils.screenshot import (
    capture_screenshot
)


# ==================================================
# CONFIG
# ==================================================

def get_config(context):

    config = configparser.ConfigParser()

    config.read(
        context.config_path
    )

    return config


# ==================================================
# USER LOGGED INTO BIGBASKET
# ==================================================

@given("user is logged into BigBasket")
def step_user_logged_in(context):

    config = get_config(context)

    base_url = config.get(
        "app",
        "base_url"
    )

    mobile = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        1
    )

    context.driver.get(
        base_url
    )

    context.login_page = LoginPage(
        context.driver
    )

    context.home_page = HomePage(
        context.driver
    )

    context.product_page = ProductPage(
        context.driver
    )

    context.cart_page = CartPage(
        context.driver
    )

    context.payment_page = PaymentPage(
        context.driver
    )

    context.login_page.click_login()

    # ==============================================
    # ASSERT LOGIN BUTTON CLICKED
    # ==============================================

    assert context.login_page.is_displayed(
        LoginLocators.MOBILE_INPUT
    ), (
        "Login Popup Not Displayed"
    )

    context.login_page.enter_mobile_email(
        mobile
    )

    context.login_page.click_continue()

    verify_clicked = False

    for _ in range(30):

        try:

            context.login_page.click_verify_continue()

            verify_clicked = True

            break

        except Exception:

            time.sleep(2)

    # ==============================================
    # ASSERT VERIFY BUTTON CLICKED
    # ==============================================

    assert verify_clicked, (
        "Verify Button Not Clicked"
    )

    time.sleep(5)

    # ==============================================
    # ASSERT LOGIN SUCCESS
    # ==============================================

    assert (
        "bigbasket"
        in context.driver.current_url.lower()
    ), (
        "Login Failed"
    )

    capture_screenshot(
        context.driver,
        "login_success"
    )


# ==================================================
# OPEN HOMEPAGE
# ==================================================

@given("the user is on the BigBasket homepage")
def step_open_homepage(context):

    config = get_config(context)

    base_url = config.get(
        "app",
        "base_url"
    )

    context.driver.get(
        base_url
    )

    # ==============================================
    # ASSERT HOMEPAGE OPENED
    # ==============================================

    assert (
        "bigbasket"
        in context.driver.current_url.lower()
    ), (
        "Homepage Not Opened"
    )

    # ==============================================
    # PAGE OBJECTS
    # ==============================================

    context.login_page = LoginPage(
        context.driver
    )

    context.home_page = HomePage(
        context.driver
    )

    context.product_page = ProductPage(
        context.driver
    )

    context.cart_page = CartPage(
        context.driver
    )

    context.payment_page = PaymentPage(
        context.driver
    )

    capture_screenshot(
        context.driver,
        "homepage_opened"
    )


# ==================================================
# CLICK LOGIN BUTTON
# ==================================================

@when("the user clicks on the login button")
def step_click_login(context):

    context.login_page.click_login()

    # ==============================================
    # ASSERT LOGIN POPUP DISPLAYED
    # ==============================================

    assert context.login_page.is_displayed(
        LoginLocators.MOBILE_INPUT
    ), (
        "Login Popup Not Displayed"
    )

    capture_screenshot(
        context.driver,
        "login_popup"
    )


# ==================================================
# ENTER MOBILE NUMBER
# ==================================================

@when("the user enters the mobile number")
def step_enter_mobile(context):

    mobile = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        1
    )

    context.login_page.enter_mobile_email(
        mobile
    )

    context.login_page.click_continue()

    # ==============================================
    # ASSERT MOBILE NUMBER ENTERED
    # ==============================================

    assert mobile is not None, (
        "Mobile Number Not Entered"
    )

    capture_screenshot(
        context.driver,
        "mobile_entered"
    )


# ==================================================
# ENTER INVALID MOBILE NUMBER
# ==================================================

@when("the user enters invalid mobile number")
def step_invalid_mobile(context):

    invalid_mobile = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        2
    )

    context.login_page.enter_mobile_email(
        invalid_mobile
    )

    context.login_page.click_continue()

    # ==============================================
    # ASSERT INVALID MOBILE ENTERED
    # ==============================================

    assert invalid_mobile is not None, (
        "Invalid Mobile Number Not Entered"
    )

    capture_screenshot(
        context.driver,
        "invalid_mobile_entered"
    )


# ==================================================
# VERIFY INVALID MOBILE ERROR
# ==================================================

@then("invalid mobile error should be displayed")
def step_invalid_mobile_error(context):

    assert context.login_page.is_displayed(
        LoginLocators.INVALID_MOBILE_POPUP
    ), (
        "Invalid Mobile Error Not Displayed"
    )

    capture_screenshot(
        context.driver,
        "invalid_mobile_error"
    )


# ==================================================
# ENTER INVALID OTP
# ==================================================

@when("the user enters invalid OTP")
def step_invalid_otp(context):

    time.sleep(15)

    context.login_page.click_verify_continue()

    capture_screenshot(
        context.driver,
        "invalid_otp_entered"
    )


# ==================================================
# VERIFY INVALID OTP ERROR
# ==================================================

@then("invalid OTP error should be displayed")
def step_invalid_otp_error(context):

    assert context.login_page.is_displayed(
        LoginLocators.INVALID_OTP_POPUP
    ), (
        "Invalid OTP Error Not Displayed"
    )

    capture_screenshot(
        context.driver,
        "invalid_otp_error"
    )


# ==================================================
# ENTER OTP
# ==================================================

@when("the user enters the OTP")
def step_enter_otp(context):

    verify_clicked = False

    for _ in range(30):

        try:

            context.login_page.click_verify_continue()

            verify_clicked = True

            break

        except Exception:

            time.sleep(2)

    # ==============================================
    # ASSERT VERIFY BUTTON CLICKED
    # ==============================================

    assert verify_clicked, (
        "Verify Button Not Clicked"
    )

    time.sleep(5)

    capture_screenshot(
        context.driver,
        "otp_verified"
    )


# ==================================================
# LOGIN SUCCESS
# ==================================================

@then("the user should be logged in successfully")
def step_login_success(context):

    assert (
        "bigbasket"
        in context.driver.current_url.lower()
    ), (
        "Login Failed"
    )

    capture_screenshot(
        context.driver,
        "login_successful"
    )