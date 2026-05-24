import os
import time
import pytest
import allure

from pages.ghee_page import GheePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

from utils.logger import LogGen
from utils.excel_reader import ExcelReader
from utils.screenshot_util import take_screenshot


logger = LogGen.loggen()


@allure.title("BigBasket End To End Flow")
@allure.description(
    "Verify Tea, Ghee, Add To Cart and Checkout Flow"
)

@pytest.mark.usefixtures("driver")
def test_bigbasket_flow(driver):

    login = LoginPage(driver)

    data = ExcelReader.read_excel(
        "login_data.xlsx",
        "Sheet1"
    )

    # =========================
    # EXCEL DATA
    # =========================

    mobile = data[0]["mobile"]

    tea_category = data[0]["category"]

    tea_name = data[0]["Tea&Ghee"]

    tea_brand = data[0]["brand"]

    ghee_category = data[1]["category"]

    ghee_name = data[1]["Tea&Ghee"]

    ghee_brand = data[1]["brand"]

    # =========================
    # PAGE OBJECTS
    # =========================

    home = HomePage(driver)

    product = ProductPage(driver)

    cart = CartPage(driver)

    ghee_page = GheePage(driver)

    logger.info(
        "Starting BigBasket Flow Test"
    )

    # =========================
    # LOGIN FLOW
    # =========================

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
        "BigBasket Website Opened Successfully"
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
        "Waiting for OTP entry in browser"
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

    logger.info(
        "Login Completed Successfully"
    )

    # LOGIN SCREENSHOT

    take_screenshot(
        driver,
        "login_success"
    )

    logger.info(
        "Login Screenshot Captured"
    )

    # =========================
    # TEA FLOW
    # =========================

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
        "Adding Tea Product to cart"
    )

    product.add_first_product_to_cart()

    time.sleep(5)

    # ASSERT

    assert (
        product.product_added_successfully()
    ), (
        "Tea Product Not Added To Cart"
    )

    # TEA SCREENSHOT

    take_screenshot(
        driver,
        "tea_product_added"
    )

    logger.info(
        "Tea Product Screenshot Captured"
    )

    # =========================
    # GHEE FLOW
    # =========================

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
        "Adding Ghee Product to cart"
    )

    ghee_page.add_first_product_to_cart()

    time.sleep(5)

    # ASSERT

    assert (
        ghee_page.product_added_successfully()
    ), (
        "Ghee Product Not Added To Cart"
    )

    # GHEE SCREENSHOT

    take_screenshot(
        driver,
        "ghee_product_added"
    )

    logger.info(
        "Ghee Product Screenshot Captured"
    )

    # =========================
    # CART FLOW
    # =========================

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

    logger.info(
        "Basket Opened Successfully"
    )

    # BASKET SCREENSHOT

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
        "Proceeding to Checkout"
    )

    cart.click_proceed()

    time.sleep(10)

    # ASSERT

    assert (
        cart.checkout_page_displayed()
    ), (
        "Checkout Page Not Displayed"
    )

    logger.info(
        "Checkout Page Opened Successfully"
    )

    # CHECKOUT SCREENSHOT

    take_screenshot(
        driver,
        "checkout_page"
    )

    logger.info(
        "Checkout Screenshot Captured"
    )

    logger.info(
        "BigBasket Flow Test Completed Successfully"
    )