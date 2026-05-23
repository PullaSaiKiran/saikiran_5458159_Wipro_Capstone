# from behave import given, when, then
#
# import configparser
# import time
#
# from locators.login_locators import LoginLocators
# from locators.product_locators import ProductLocators
#
# from pages.login_page import LoginPage
# from pages.home_page import HomePage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from pages.payment_page import PaymentPage
#
# from utils.screenshot import (
#     capture_screenshot
# )
#
# from utils.excel_reader import (
#     ExcelReader
# )
#
#
# # ==================================================
# # CONFIG
# # ==================================================
#
# def get_config(context):
#
#     config = configparser.ConfigParser()
#
#     config.read(
#         context.config_path
#     )
#
#     return config
#
#
# # ==================================================
# # COMMON LOGIN
# # ==================================================
#
# @given("user is logged into BigBasket")
# def step_user_logged_in(context):
#
#     config = get_config(context)
#
#     base_url = config.get(
#         "app",
#         "base_url"
#     )
#
#     # ==============================================
#     # MOBILE NUMBER FROM EXCEL
#     # ==============================================
#
#     mobile = ExcelReader.get_data(
#         "data/test_data.xlsx",
#         "Sheet1",
#         2,
#         1
#     )
#
#     # ==============================================
#     # OPEN WEBSITE
#     # ==============================================
#
#     context.driver.get(
#         base_url
#     )
#
#     assert (
#         "bigbasket"
#         in context.driver.current_url.lower()
#     ), "Homepage Not Opened"
#
#     # ==============================================
#     # PAGE OBJECTS
#     # ==============================================
#
#     context.login_page = LoginPage(
#         context.driver
#     )
#
#     context.home_page = HomePage(
#         context.driver
#     )
#
#     context.product_page = ProductPage(
#         context.driver
#     )
#
#     context.cart_page = CartPage(
#         context.driver
#     )
#
#     # ==============================================
#     # LOGIN FLOW
#     # ==============================================
#
#     context.login_page.click_login()
#
#     context.login_page.enter_mobile_email(
#         mobile
#     )
#
#     context.login_page.click_continue()
#
#     print(
#         "\nEnter OTP manually in browser..."
#     )
#
#     verify_clicked = False
#
#     for _ in range(30):
#
#         try:
#
#             context.login_page.click_verify_continue()
#
#             verify_clicked = True
#
#             break
#
#         except Exception:
#
#             time.sleep(2)
#
#     assert verify_clicked, \
#         "Verify Button Not Clicked"
#
#     time.sleep(5)
#
#     capture_screenshot(
#         context.driver,
#         "login_success"
#     )
#
#     print(
#         "Login Successful"
#     )
#
#
# # ==================================================
# # INVALID MOBILE
# # ==================================================
#
# @when("the user enters invalid mobile number")
# def step_invalid_mobile(context):
#
#     invalid_mobile = ExcelReader.get_data(
#         "data/test_data.xlsx",
#         "Sheet1",
#         2,
#         2
#     )
#
#     context.login_page.enter_mobile_email(
#         invalid_mobile
#     )
#
#     context.login_page.click_continue()
#
#
# @then("invalid mobile error should be displayed")
# def step_invalid_mobile_error(context):
#
#     assert context.login_page.is_displayed(
#         LoginLocators.INVALID_MOBILE_POPUP
#     ), "Invalid Mobile Error Not Displayed"
#
#     capture_screenshot(
#         context.driver,
#         "invalid_mobile_error"
#     )
#
#
# # ==================================================
# # INVALID OTP
# # ==================================================
#
# @when("the user enters invalid OTP")
# def step_invalid_otp(context):
#
#     print(
#         "\nEnter Invalid OTP manually..."
#     )
#
#     time.sleep(15)
#
#     context.login_page.click_verify_continue()
#
#
# @then("invalid OTP error should be displayed")
# def step_invalid_otp_error(context):
#
#     assert context.login_page.is_displayed(
#         LoginLocators.INVALID_OTP_POPUP
#     ), "Invalid OTP Error Not Displayed"
#
#     capture_screenshot(
#         context.driver,
#         "invalid_otp_error"
#     )
#
#
# # ==================================================
# # INVALID CARD
# # ==================================================
#
# @when("the user enters invalid card number")
# def step_invalid_card(context):
#
#     context.payment_page = PaymentPage(
#         context.driver
#     )
#
#     context.payment_page.enter_invalid_card_number()
#
#
# @then("invalid card error should be displayed")
# def step_invalid_card_error(context):
#
#     context.payment_page.verify_invalid_card_error()
#
#     capture_screenshot(
#         context.driver,
#         "invalid_card_error"
#     )
#
#     print(
#         "Invalid Card Error Verified"
#     )
#
# # ==========================================
# # SEARCH TEA PRODUCT
# # ==========================================
#
# def search_tea_product(
#         self,
#         product_name
# ):
#
#     self.scroll_to_element(
#         ProductLocators.BRAND_SEARCH_BOX
#     )
#
#     self.enter_text(
#         ProductLocators.BRAND_SEARCH_BOX,
#         product_name
#     )
#
# # ==================================================
# # SELECT TEA CHECKBOX
# # ==================================================
#
# @when("the user selects Tea checkbox")
# def step_select_tea_checkbox(context):
#
#     context.product_page.select_tea_checkbox()
#
#
# # ==================================================
# # VERIFY FILTERED PRODUCTS
# # ==================================================
#
# @then("filtered Tea products should be displayed")
# def step_verify_filtered_products(context):
#
#     context.product_page.verify_filtered_products()
#
#     capture_screenshot(
#         context.driver,
#         "filtered_tea_products"
#     )
#
#     print(
#         "Filtered Tea Products Displayed"
#     )
#
#
# # ==================================================
# # ADD TEA PRODUCT
# # ==================================================
#
# @when("the user adds Tea product to cart")
# def step_add_tea_product(context):
#
#     context.product_page.add_tea_product()
#
#     print(
#         "Tea Product Added"
#     )
#
#
# # ==================================================
# # DELETE PRODUCT
# # ==================================================
#
# @when("the user deletes the Tea product")
# def step_delete_product(context):
#
#     context.cart_page.delete_product()
#
#
# @then("the Tea product should be removed successfully")
# def step_verify_removed(context):
#
#     context.cart_page.verify_product_removed()
#
#     capture_screenshot(
#         context.driver,
#         "product_removed"
#     )
#
#     print(
#         "Product Removed Successfully"
#     )
#
#
# # ==================================================
# # RELEVANCE DROPDOWN
# # ==================================================
#
# @when("the user clicks on Relevance dropdown")
# def step_click_relevance(context):
#
#     context.product_page.click_relevance_dropdown()
#
#
# @when("the user selects Price Low To High")
# def step_select_price(context):
#
#     context.product_page.select_price_low_to_high()
#
#
# @then("sorted Ghee products should be displayed")
# def step_verify_sorted_products(context):
#
#     context.product_page.verify_sorted_ghee_products()
#
#     capture_screenshot(
#         context.driver,
#         "sorted_ghee_products"
#     )
#
#
# # ==================================================
# # INVALID TEA PRODUCT SEARCH
# # ==================================================
#
# @when("the user searches invalid Tea product")
# def step_search_invalid_tea(context):
#
#     invalid_product = ExcelReader.get_data(
#         "data/test_data.xlsx",
#         "Sheet1",
#         2,
#         4
#     )
#
#     context.product_page.search_invalid_tea_product(
#         invalid_product
#     )
#
#
# @then("no results should be displayed")
# def step_verify_no_results(context):
#
#     context.product_page.verify_no_results_found()
#
#     capture_screenshot(
#         context.driver,
#         "no_results_found"
#     )