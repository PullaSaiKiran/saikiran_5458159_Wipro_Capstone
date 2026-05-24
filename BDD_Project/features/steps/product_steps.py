from behave import when, then
from locators.product_locators import ProductLocators
from utils.screenshot import capture_screenshot
from utils.excel_reader import ExcelReader


# ==================================================
# CLICK TEA FROM HOMEPAGE
# ==================================================
@when("the user clicks on Tea from the homepage")
def step_click_tea(context):
    context.home_page.click_tea()
    capture_screenshot(context.driver, "tea_page")
    assert "tea" in context.driver.current_url.lower(), "Not navigated to Tea page"


# ==================================================
# SEARCH TEA PRODUCT
# ==================================================
@when("the user searches for Tea product")
def step_search_tea_product(context):
    tea_product = ExcelReader.get_data("data/test_data.xlsx", "Sheet1", 2, 3)
    context.product_page.search_tea_product(tea_product)
    capture_screenshot(context.driver, "tea_search")
    assert context.product_page.is_displayed(
        ProductLocators.BRAND_SEARCH_BOX
    ), (
        "Tea Search Failed"
    )


# ==================================================
# SELECT TEA CHECKBOX
# ==================================================
@when("the user selects Tea checkbox")
def step_select_tea_checkbox(context):
    context.product_page.select_tea_checkbox()
    capture_screenshot(context.driver, "tea_checkbox")
    assert context.product_page.is_displayed(ProductLocators.FILTERED_PRODUCT), "Tea checkbox selection failed"


# ==================================================
# VERIFY FILTERED PRODUCTS
# ==================================================
@then("filtered Tea products should be displayed")
def step_verify_filtered_products(context):
    context.product_page.verify_filtered_products()
    capture_screenshot(context.driver, "filtered_tea_products")
    assert context.product_page.is_displayed(ProductLocators.FILTERED_PRODUCT), "Filtered Tea products not displayed"


# ==================================================
# APPLY BRAND FILTER
# ==================================================
@when("the user applies brand filter on Tea page")
def step_apply_brand_filter(context):
    context.product_page.apply_brand_filter()
    capture_screenshot(context.driver, "brand_filter")
    assert context.product_page.is_displayed(ProductLocators.BRAND_CHAI_POINT), "Brand filter not applied"


# ==================================================
# ADD FIRST TEA PRODUCT
# ==================================================
@when("the user adds the first Tea product to cart")
def step_add_first_product(context):
    context.product_page.add_first_product_to_cart()
    capture_screenshot(context.driver, "first_product_added")
    assert context.product_page.is_displayed(ProductLocators.INCREMENT_BUTTON), "Tea Product Not Added"


# ==================================================
# CLICK GHEE FROM HOMEPAGE
# ==================================================
@when("the user clicks on Ghee from the homepage")
def step_click_ghee(context):
    context.home_page.click_ghee()
    capture_screenshot(context.driver, "ghee_page")
    assert "ghee" in context.driver.current_url.lower(), "Not navigated to Ghee page"


# ==================================================
# APPLY GHEE FILTER
# ==================================================
@when("the user applies brand filter on Ghee page")
def step_apply_ghee_filter(context):
    context.product_page.click_ghee_vanaspati()
    context.product_page.apply_brand_amul()
    capture_screenshot(context.driver, "ghee_brand_filter")
    assert context.product_page.is_displayed(ProductLocators.BRAND_AMUL), "Ghee brand filter not applied"


# ==================================================
# ADD GHEE PRODUCT
# ==================================================
@when("the user adds the first Ghee product to cart")
def step_add_ghee(context):
    context.product_page.add_first_product_to_cart()
    capture_screenshot(context.driver, "first_ghee_added")
    assert context.product_page.is_displayed(ProductLocators.INCREMENT_BUTTON), "Ghee Product Not Added"


# ==================================================
# VERIFY GHEE PRODUCT
# ==================================================
@then("the Ghee product should be added successfully")
def step_verify_ghee(context):
    assert context.product_page.is_displayed(ProductLocators.INCREMENT_BUTTON), "Ghee product not verified"
    capture_screenshot(context.driver, "ghee_product_verified")


# ==================================================
# GO BACK TO HOMEPAGE
# ==================================================
@when("the user goes back to the homepage")
def step_go_home(context):
    context.driver.get("https://www.bigbasket.com")
    capture_screenshot(context.driver, "homepage")
    assert "bigbasket" in context.driver.current_url.lower(), "Failed to navigate to homepage"