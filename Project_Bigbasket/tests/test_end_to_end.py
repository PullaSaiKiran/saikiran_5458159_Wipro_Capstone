import os
import pytest
import allure

from selenium.webdriver.support.ui import (
    WebDriverWait
)

from selenium.webdriver.support import (
    expected_conditions as EC
)

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

    wait = WebDriverWait(
        driver,
        20
    )

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

    wait.until(
        lambda d:
        "bigbasket"
        in d.current_url.lower()
    )

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

    wait.until(
        lambda d:
        login.login_popup_displayed()
    )

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

    input(
        "Enter OTP Manually "
        "And Press ENTER..."
    )

    logger.info(
        "Clicking Verify & Continue"
    )

    login.click_verify_continue()

    wait.until(
        lambda d:
        login.login_successful()
    )

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
        f"Navigating To {tea_category}"
    )

    home.click_tea()

    wait.until(
        lambda d:
        product.tea_page_displayed()
    )

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

    wait.until(
        lambda d:
        product.exotic_tea_displayed()
    )

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

    wait.until(
        lambda d:
        product.brand_filter_applied(
            tea_brand
        )
    )

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

    wait.until(
        lambda d:
        product.product_added_successfully()
    )

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
        f"Navigating To {ghee_category}"
    )

    home.click_ghee()

    wait.until(
        lambda d:
        ghee_page.ghee_page_displayed()
    )

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

    wait.until(
        lambda d:
        ghee_page.ghee_category_displayed()
    )

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

    wait.until(
        lambda d:
        ghee_page.brand_filter_applied(
            ghee_brand
        )
    )

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

    wait.until(
        lambda d:
        ghee_page.product_added_successfully()
    )

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

    wait.until(
        lambda d:
        cart.cart_page_displayed()
    )

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
        "Proceeding To Checkout"
    )

    cart.click_proceed()

    wait.until(
        lambda d:
        cart.checkout_page_displayed()
    )

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