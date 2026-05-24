import time
import pytest
import allure

from pages.cart_page import CartPage
from pages.ghee_page import GheePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

from utils.logger import LogGen
from utils.excel_reader import ExcelReader
from utils.screenshot_util import take_screenshot


logger = LogGen.loggen()


# ==========================================
# EXCEL DATA
# ==========================================

data = ExcelReader.read_excel(
    "login_data.xlsx",
    "Sheet1"
)

mobile = data[0]["mobile"]

tea_category = data[0]["category"]

tea_name = data[0]["Tea&Ghee"]

tea_brand = data[0]["brand"]

ghee_category = data[1]["category"]

ghee_name = data[1]["Tea&Ghee"]

ghee_brand = data[1]["brand"]


# ==========================================
# TEST CASE 1
# VALID LOGIN
# ==========================================

@allure.title("Valid Login Test")

@pytest.mark.order(1)
@pytest.mark.usefixtures("driver")
def test_valid_login(driver):

    login = LoginPage(driver)

    logger.info(
        "Opening BigBasket Website"
    )

    login.open_bigbasket()

    time.sleep(5)

    # ASSERT

    assert (
        "bigbasket"
        in driver.current_url.lower()
    ), (
        "BigBasket Website Not Opened"
    )

    logger.info(
        "Clicking Login Button"
    )

    login.click_login()

    time.sleep(3)

    # ASSERT

    assert (
        login.login_popup_displayed()
    ), (
        "Login Popup Not Displayed"
    )

    logger.info(
        "Entering Mobile Number"
    )

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    # ASSERT

    entered_mobile = login.get_mobile_value()

    assert (
        entered_mobile == mobile
    ), (
        "Mobile Number Not Entered Properly"
    )

    logger.info(
        "Clicking Continue Button"
    )

    login.click_continue()

    logger.info(
        "Waiting For OTP Entry"
    )

    time.sleep(30)

    logger.info(
        "Clicking Verify & Continue"
    )

    login.click_verify_continue()

    time.sleep(10)

    # ASSERT

    assert (
        login.login_successful()
    ), (
        "Login Failed"
    )

    take_screenshot(
        driver,
        "valid_login"
    )

    logger.info(
        "Login Screenshot Captured"
    )

    logger.info(
        "Valid Login Test Passed"
    )


# ==========================================
# TEST CASE 2
# TEA FLOW
# ==========================================

@allure.title("Tea Flow Test")

@pytest.mark.order(2)
@pytest.mark.usefixtures("driver")
def test_tea_flow(driver):

    login = LoginPage(driver)

    home = HomePage(driver)

    product = ProductPage(driver)

    # LOGIN

    login.open_bigbasket()

    time.sleep(5)

    login.click_login()

    time.sleep(3)

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    login.click_continue()

    time.sleep(30)

    login.click_verify_continue()

    time.sleep(10)

    # ASSERT

    assert (
        login.login_successful()
    ), (
        "Login Failed"
    )

    # TEA FLOW

    logger.info(
        f"Navigating to {tea_category}"
    )

    home.click_tea()

    time.sleep(10)

    # ASSERT

    assert (
        product.tea_page_displayed()
    ), (
        "Tea Page Not Displayed"
    )

    logger.info(
        f"Selecting {tea_name}"
    )

    product.filter_exotic_tea()

    time.sleep(8)

    # ASSERT

    assert (
        product.exotic_tea_displayed()
    ), (
        "Exotic Tea Category Not Displayed"
    )

    logger.info(
        f"Applying Brand Filter: {tea_brand}"
    )

    product.apply_brand_chai_point()

    time.sleep(8)

    # ASSERT

    assert (
        product.brand_filter_applied(
            tea_brand
        )
    ), (
        "Tea Brand Filter Not Applied"
    )

    logger.info(
        "Tea Brand Filter Applied Successfully"
    )

    logger.info(
        "Adding Tea Product To Cart"
    )

    product.add_first_product_to_cart()

    time.sleep(5)

    # ASSERT

    assert (
        product.product_added_successfully()
    ), (
        "Tea Product Not Added To Cart"
    )

    take_screenshot(
        driver,
        "tea_product_added"
    )

    logger.info(
        "Tea Product Screenshot Captured"
    )

    logger.info(
        "Tea Flow Test Passed"
    )


# ==========================================
# TEST CASE 3
# GHEE FLOW
# ==========================================

@allure.title("Ghee Flow Test")

@pytest.mark.order(3)
@pytest.mark.usefixtures("driver")
def test_ghee_flow(driver):

    login = LoginPage(driver)

    home = HomePage(driver)

    ghee_page = GheePage(driver)

    # LOGIN

    login.open_bigbasket()

    time.sleep(5)

    login.click_login()

    time.sleep(3)

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    login.click_continue()

    time.sleep(30)

    login.click_verify_continue()

    time.sleep(10)

    # ASSERT

    assert (
        login.login_successful()
    ), (
        "Login Failed"
    )

    # GHEE FLOW

    logger.info(
        f"Navigating to {ghee_category}"
    )

    home.click_ghee()

    time.sleep(15)

    # ASSERT

    assert (
        ghee_page.ghee_page_displayed()
    ), (
        "Ghee Page Not Displayed"
    )

    logger.info(
        f"Selecting {ghee_name}"
    )

    ghee_page.click_ghee_vanaspati()

    time.sleep(10)

    # ASSERT

    assert (
        ghee_page.ghee_category_displayed()
    ), (
        "Ghee Category Not Displayed"
    )

    logger.info(
        f"Applying Brand Filter: {ghee_brand}"
    )

    ghee_page.apply_brand_amul()

    time.sleep(15)

    # ASSERT

    assert (
        ghee_page.brand_filter_applied(
            ghee_brand
        )
    ), (
        "Ghee Brand Filter Not Applied"
    )

    logger.info(
        "Ghee Brand Filter Applied Successfully"
    )

    logger.info(
        "Adding Ghee Product To Cart"
    )

    ghee_page.add_first_product_to_cart()

    time.sleep(5)

    # ASSERT

    assert (
        ghee_page.product_added_successfully()
    ), (
        "Ghee Product Not Added To Cart"
    )

    take_screenshot(
        driver,
        "ghee_product_added"
    )

    logger.info(
        "Ghee Product Screenshot Captured"
    )

    logger.info(
        "Ghee Flow Test Passed"
    )


# ==========================================
# TEST CASE 4
# CHECKOUT FLOW
# ==========================================

@allure.title("Checkout Flow Test")

@pytest.mark.order(4)
@pytest.mark.usefixtures("driver")
def test_checkout_flow(driver):

    login = LoginPage(driver)

    home = HomePage(driver)

    cart = CartPage(driver)

    # LOGIN

    login.open_bigbasket()

    time.sleep(5)

    login.click_login()

    time.sleep(3)

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    login.click_continue()

    time.sleep(30)

    login.click_verify_continue()

    time.sleep(10)

    # ASSERT

    assert (
        login.login_successful()
    ), (
        "Login Failed"
    )

    # BASKET FLOW

    logger.info(
        "Opening Basket"
    )

    home.click_basket()

    time.sleep(10)

    # ASSERT

    assert (
        cart.cart_page_displayed()
    ), (
        "Cart Page Not Opened"
    )

    take_screenshot(
        driver,
        "basket_opened"
    )

    logger.info(
        "Basket Screenshot Captured"
    )

    # ASSERT

    assert (
        cart.cart_has_products()
    ), (
        "Products Not Present In Cart"
    )

    logger.info(
        "Proceeding To Checkout"
    )

    cart.click_proceed()

    time.sleep(10)

    # ASSERT

    assert (
        cart.checkout_page_displayed()
    ), (
        "Checkout Page Not Displayed"
    )

    take_screenshot(
        driver,
        "checkout_page"
    )

    logger.info(
        "Checkout Screenshot Captured"
    )

    logger.info(
        "Checkout Flow Test Passed"
    )


# ==========================================
# TEST CASE 5
# INVALID MOBILE NUMBER
# ==========================================

@allure.title("Invalid Mobile Number Test")

@pytest.mark.order(5)
@pytest.mark.usefixtures("driver")
def test_invalid_phone(driver):

    login = LoginPage(driver)

    logger.info(
        "Opening BigBasket Website"
    )

    login.open_bigbasket()

    time.sleep(5)

    login.click_login()

    time.sleep(3)

    # ASSERT

    assert (
        login.login_popup_displayed()
    ), (
        "Login Popup Not Displayed"
    )

    logger.info(
        "Entering Invalid Mobile Number"
    )

    login.enter_mobile_email(
        "1234565470"
    )

    time.sleep(2)

    login.click_continue()

    time.sleep(3)

    take_screenshot(
        driver,
        "invalid_mobile"
    )

    logger.info(
        "Invalid Mobile Screenshot Captured"
    )

    # ASSERT

    assert (
        login.invalid_mobile_error_displayed()
    ), (
        "Invalid Mobile Error Not Displayed"
    )

    logger.info(
        "Invalid Mobile Test Passed"
    )


# ==========================================
# TEST CASE 6
# INVALID OTP
# ==========================================

@allure.title("Invalid OTP Test")

@pytest.mark.order(6)
@pytest.mark.usefixtures("driver")
def test_invalid_otp(driver):

    login = LoginPage(driver)

    logger.info(
        "Opening BigBasket Website"
    )

    login.open_bigbasket()

    time.sleep(5)

    login.click_login()

    time.sleep(3)

    login.enter_mobile_email(
        mobile
    )

    time.sleep(3)

    login.click_continue()

    time.sleep(5)

    logger.info(
        "Enter Invalid OTP Manually"
    )

    time.sleep(15)

    login.click_verify_continue()

    time.sleep(5)

    take_screenshot(
        driver,
        "invalid_otp"
    )

    logger.info(
        "Invalid OTP Screenshot Captured"
    )

    # ASSERT

    assert (
        login.invalid_otp_error_displayed()
    ), (
        "Invalid OTP Error Not Displayed"
    )

    logger.info(
        "Invalid OTP Test Passed"
    )