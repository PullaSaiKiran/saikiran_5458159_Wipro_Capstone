from behave import when, then
from utils.screenshot import capture_screenshot

# ==================================================
# ADD TEA PRODUCT TO CART
# ==================================================
@when("the user adds Tea product to cart")
def step_add_tea_product(context):
    context.product_page.add_tea_product()

    # Assert the product is visible in product list/cart badge
    assert context.product_page.is_tea_product_visible(), "Tea product was not visible after adding"

    capture_screenshot(context.driver, "tea_product_added")


# ==================================================
# NAVIGATE TO CART PAGE
# ==================================================
@when("the user navigates to the cart page")
def step_navigate_cart(context):
    context.cart_page.open_cart()

    # Assert cart page is displayed
    assert "cart" in context.driver.current_url.lower(), "Cart page did not open correctly"

    capture_screenshot(context.driver, "cart_page")


# ==================================================
# VERIFY PRODUCT ADDED
# ==================================================
@then("the Tea product should be added successfully")
def step_verify_product_added(context):
    assert context.cart_page.is_product_in_cart("Tata Tea Chakra Gold"), "Tea Product Not Added To Cart"
    capture_screenshot(context.driver, "tea_product_verified")


# ==================================================
# DELETE TEA PRODUCT
# ==================================================
@when("the user deletes the Tea product")
def step_delete_product(context):
    context.cart_page.delete_product()

    # Assert product is removed from cart
    assert not context.cart_page.is_product_in_cart("Tata Tea Chakra Gold"), "Tea Product Not Removed From Cart"

    capture_screenshot(context.driver, "product_deleted")


# ==================================================
# VERIFY PRODUCT REMOVED
# ==================================================
@then("the Tea product should be removed successfully")
def step_verify_removed(context):
    assert not context.cart_page.is_product_in_cart("Tata Tea Chakra Gold"), "Tea Product Still Present In Cart"
    capture_screenshot(context.driver, "product_removed")


# ==================================================
# VERIFY CART ITEMS
# ==================================================
@then("the cart should contain added products")
def step_verify_cart(context):
    # You can check multiple products added
    assert context.cart_page.get_cart_items_count() > 0, "Cart is empty"
    capture_screenshot(context.driver, "cart_has_items")


# ==================================================
# VERIFY CHECKOUT PAGE
# ==================================================
@then("the checkout page should be displayed")
def step_checkout_page(context):
    assert "checkout" in context.driver.current_url.lower(), "Checkout page not displayed"
    capture_screenshot(context.driver, "checkout_page")