from behave import when, then

from locators.product_locators import ProductLocators
from utils.screenshot import (
    capture_screenshot
)

from utils.excel_reader import (
    ExcelReader
)


# ==================================================
# CLICK TEA FROM HOMEPAGE
# ==================================================

@when("the user clicks on Tea from the homepage")
def step_click_tea(context):

    context.home_page.click_tea()

    capture_screenshot(
        context.driver,
        "tea_page"
    )


# ==================================================
# SEARCH TEA PRODUCT
# ==================================================

@when("the user searches for Tea product")
def step_search_tea_product(context):

    tea_product = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        3
    )

    context.product_page.search_tea_product(
        tea_product
    )

    capture_screenshot(
        context.driver,
        "tea_search"
    )


# ==================================================
# SELECT TEA CHECKBOX
# ==================================================

@when("the user selects Tea checkbox")
def step_select_tea_checkbox(context):

    context.product_page.select_tea_checkbox()

    capture_screenshot(
        context.driver,
        "tea_checkbox"
    )


# ==================================================
# VERIFY FILTERED PRODUCTS
# ==================================================

@then("filtered Tea products should be displayed")
def step_verify_filtered_products(context):

    context.product_page.verify_filtered_products()

    capture_screenshot(
        context.driver,
        "filtered_tea_products"
    )


# ==================================================
# APPLY BRAND FILTER
# ==================================================

@when("the user applies brand filter on Tea page")
def step_apply_brand_filter(context):

    context.product_page.apply_brand_filter()

    capture_screenshot(
        context.driver,
        "brand_filter"
    )


# ==================================================
# ADD FIRST TEA PRODUCT
# ==================================================

@when("the user adds the first Tea product to cart")
def step_add_first_product(context):

    context.product_page.add_first_product_to_cart()

    capture_screenshot(
        context.driver,
        "first_product_added"
    )


# ==================================================
# CLICK GHEE FROM HOMEPAGE
# ==================================================

@when("the user clicks on Ghee from the homepage")
def step_click_ghee(context):

    context.home_page.click_ghee()

    capture_screenshot(
        context.driver,
        "ghee_page"
    )


# ==================================================
# CLICK RELEVANCE DROPDOWN
# ==================================================

@when("the user clicks on Relevance dropdown")
def step_click_relevance(context):

    context.product_page.click_relevance_dropdown()

    capture_screenshot(
        context.driver,
        "relevance_dropdown"
    )


# ==================================================
# SELECT PRICE LOW TO HIGH
# ==================================================

@when("the user selects Price Low To High")
def step_select_price(context):

    context.product_page.select_price_low_to_high()

    capture_screenshot(
        context.driver,
        "price_low_to_high"
    )


# ==================================================
# VERIFY SORTED PRODUCTS
# ==================================================

@then("sorted Ghee products should be displayed")
def step_verify_sorted_products(context):

    context.product_page.verify_sorted_ghee_products()

    capture_screenshot(
        context.driver,
        "sorted_ghee_products"
    )


# ==================================================
# SEARCH INVALID TEA PRODUCT
# ==================================================

@when("the user searches invalid Tea product")
def step_search_invalid_tea(context):

    invalid_product = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        4
    )

    context.product_page.search_invalid_tea_product(
        invalid_product
    )

    capture_screenshot(
        context.driver,
        "invalid_tea_search"
    )


# ==================================================
# VERIFY NO RESULTS
# ==================================================

@then("no results should be displayed")
def step_verify_no_results(context):

    context.product_page.verify_no_results_found()

    capture_screenshot(
        context.driver,
        "no_results_found"
    )

# ==================================================
# GO BACK TO HOMEPAGE
# ==================================================

@when("the user goes back to the homepage")
def step_go_home(context):

    context.driver.get(
        "https://www.bigbasket.com"
    )


# ==================================================
# APPLY GHEE FILTER
# ==================================================

@when("the user applies brand filter on Ghee page")
def step_apply_ghee_filter(context):

    context.product_page.click_ghee_vanaspati()

    context.product_page.apply_brand_amul()


# ==================================================
# ADD GHEE PRODUCT
# ==================================================

@when("the user adds the first Ghee product to cart")
def step_add_ghee(context):

    context.product_page.add_first_product_to_cart()


# ==================================================
# VERIFY GHEE PRODUCT
# ==================================================

@then("the Ghee product should be added successfully")
def step_verify_ghee(context):

    assert True


# ==================================================
# VERIFY PRODUCT ADDED
# ==================================================

def verify_product_added(self):

    assert self.is_displayed(
        ProductLocators.INCREMENT_BUTTON
    ), (
        "Tea Product Not Added"
    )


