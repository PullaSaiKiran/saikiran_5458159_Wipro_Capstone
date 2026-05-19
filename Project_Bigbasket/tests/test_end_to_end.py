import time
import pytest

from pages.ghee_page import GheePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.logger import LogGen
from utils.excel_reader import ExcelReader
logger = LogGen.loggen()

@pytest.mark.usefixtures("driver")
def test_bigbasket_flow(driver):
    login = LoginPage(driver)

    data = ExcelReader.read_excel(
        "login_data.xlsx",
        "Sheet1"
    )
    mobile = data[0]["mobile"]
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    logger.info("Starting BigBasket Flow Test")


    logger.info("Opening BigBasket Website")
    login.open_bigbasket()
    time.sleep(5)

    logger.info("Clicking Login Button")
    login.click_login()
    time.sleep(3)

    logger.info("Entering Mobile Number")
    login.enter_mobile_email(mobile)
    time.sleep(3)

    logger.info("Clicking Continue Button")
    login.click_continue()

    logger.info("Waiting for OTP entry in browser")
    time.sleep(30)   # manually enter OTP

    logger.info("Clicking Verify & Continue")
    login.click_verify_continue()
    time.sleep(25)

    logger.info("Login Completed Successfully")

    # --- TEA FLOW ---
    logger.info("Navigating to Tea category")
    home.click_tea()
    time.sleep(10)

    logger.info("Selecting Exotic & Flavoured Tea")
    product.filter_exotic_tea()
    time.sleep(8)

    logger.info("Applying Brand Filter: 6rasa")
    product.apply_brand_chai_point()
    time.sleep(8)

    logger.info("Adding first product to cart")
    product.add_first_product_to_cart()
    time.sleep(5)

    # # Increase Quantity
    # product.click_increment()
    # time.sleep(5)

    # --- GHEE FLOW ---
    logger.info("Navigating to Ghee category")
    home.click_ghee()
    time.sleep(15)
    logger.info("Selecting Ghee & Vanaspati")
    ghee_page = GheePage(driver)  # or GheePage if you split classes
    ghee_page.click_ghee_vanaspati()
    time.sleep(10)

    ghee_page.apply_brand_amul()
    time.sleep(15)

    logger.info("Adding first product to cart")
    product.add_first_product_to_cart()
    time.sleep(5)

    logger.info("Opening cart")
    # Open Basket
    home.click_basket()
    time.sleep(10)

    logger.info("Proceeding to checkout")
    cart.click_proceed()
    time.sleep(10)

    logger.info("BigBasket Flow Test Completed Successfully")
    print("Checkout Page Opened Successfully")