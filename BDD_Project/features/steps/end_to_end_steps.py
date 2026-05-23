# from behave import given, when, then
#
# import configparser
# import time
#
# from pages.login_page import LoginPage
# from pages.home_page import HomePage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
#
# from utils.screenshot import (
#     capture_screenshot
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
# # BACKGROUND
# # ==================================================
#
# @given("the user is on the BigBasket homepage")
# def step_open_homepage(context):
#
#     config = get_config(context)
#
#     base_url = config.get(
#         "app",
#         "base_url"
#     )
#
#     context.driver.get(
#         base_url
#     )
#
#     assert (
#         "bigbasket"
#         in context.driver.current_url.lower()
#     ), "BigBasket Homepage Not Opened"
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
#
# # ==================================================
# # LOGIN FLOW
# # ==================================================
#
# @when("the user clicks on the login button")
# def step_click_login(context):
#
#     context.login_page.click_login()
#
#
# @when("the user enters the mobile number")
# def step_enter_mobile(context):
#
#     config = get_config(context)
#
#     mobile = config.get(
#         "app",
#         "mobile_number"
#     )
#
#     context.login_page.enter_mobile_email(
#         mobile
#     )
#
#     context.login_page.click_continue()
#
#
# @when("the user enters the OTP")
# def step_enter_otp(context):
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
#         "Verify button not clicked"
#
#     time.sleep(5)
#
#
# @then("the user should be logged in successfully")
# def step_login_success(context):
#
#     assert (
#         "bigbasket"
#         in context.driver.current_url.lower()
#     ), "Login Failed"
#
#     capture_screenshot(
#         context.driver,
#         "login_success"
#     )
#
#
# # ==================================================
# # TEA FLOW
# # ==================================================
#
# @when("the user clicks on Tea from the homepage")
# def step_click_tea(context):
#
#     context.home_page.click_tea()
#
#
# @when("the user applies brand filter on Tea page")
# def step_apply_tea_filter(context):
#
#     context.product_page.filter_exotic_tea()
#
#     context.product_page.apply_brand_chai_point()
#
#
# @when("the user adds the first Tea product to cart")
# def step_add_tea_product(context):
#
#     context.product_page.add_first_product_to_cart()
#
#
# @then("the Tea product should be added successfully")
# def step_verify_tea_added(context):
#
#     capture_screenshot(
#         context.driver,
#         "tea_product_added"
#     )
#
#     assert True
#
#
# # ==================================================
# # RETURN HOME
# # ==================================================
#
# @when("the user goes back to the homepage")
# def step_go_home(context):
#
#     config = get_config(context)
#
#     base_url = config.get(
#         "app",
#         "base_url"
#     )
#
#     context.driver.get(
#         base_url
#     )
#
#     time.sleep(3)
#
#     assert (
#         "bigbasket"
#         in context.driver.current_url.lower()
#     ), "Homepage Not Opened"
#
#
# # ==================================================
# # GHEE FLOW
# # ==================================================
#
# @when("the user clicks on Ghee from the homepage")
# def step_click_ghee(context):
#
#     context.home_page.click_ghee()
#
#
# @when("the user applies brand filter on Ghee page")
# def step_apply_ghee_filter(context):
#
#     context.product_page.click_ghee_vanaspati()
#
#     context.product_page.apply_brand_amul()
#
#
# @when("the user adds the first Ghee product to cart")
# def step_add_ghee_product(context):
#
#     context.product_page.add_first_product_to_cart()
#
#
# @then("the Ghee product should be added successfully")
# def step_verify_ghee_added(context):
#
#     capture_screenshot(
#         context.driver,
#         "ghee_product_added"
#     )
#
#     assert True
#
#
# # ==================================================
# # CART FLOW
# # ==================================================
#
# @when("the user navigates to the cart page")
# def step_open_cart(context):
#
#     context.cart_page.open_cart()
#
#
# @then("the cart should contain added products")
# def step_verify_cart(context):
#
#     context.cart_page.verify_cart_has_items()
#
#     capture_screenshot(
#         context.driver,
#         "cart_page"
#     )
#
#
# # ==================================================
# # CHECKOUT FLOW
# # ==================================================
#
# @when("the user clicks on Proceed to Checkout")
# def step_click_checkout(context):
#
#     context.cart_page.click_proceed()
#
#
# @then("the checkout page should be displayed")
# def step_verify_checkout(context):
#
#     context.cart_page.verify_checkout_page()
#
#     capture_screenshot(
#         context.driver,
#         "checkout_page"
#     )
# @when("the user normalizes Tea product quantity")
# def step_normalize_quantity(context):
#
#     context.product_page.normalize_product_quantity()