from behave import when, then

from utils.screenshot import (
    capture_screenshot
)


# ==================================================
# ADD TEA PRODUCT TO CART
# ==================================================

@when("the user adds Tea product to cart")
def step_add_tea_product(context):

    context.product_page.add_tea_product()

    capture_screenshot(
        context.driver,
        "tea_product_added"
    )


# ==================================================
# NAVIGATE TO CART PAGE
# ==================================================

@when("the user navigates to the cart page")
def step_navigate_cart(context):

    context.cart_page.open_cart()

    capture_screenshot(
        context.driver,
        "cart_page"
    )


# ==================================================
# VERIFY PRODUCT ADDED
# ==================================================

@then("the Tea product should be added successfully")
def step_verify_product_added(context):

    context.cart_page.verify_product_added()

    capture_screenshot(
        context.driver,
        "tea_product_verified"
    )


# ==================================================
# DELETE TEA PRODUCT
# ==================================================

@when("the user deletes the Tea product")
def step_delete_product(context):

    context.cart_page.delete_product()

    capture_screenshot(
        context.driver,
        "product_deleted"
    )


# ==================================================
# VERIFY PRODUCT REMOVED
# ==================================================

@then("the Tea product should be removed successfully")
def step_verify_removed(context):

    context.cart_page.verify_product_removed()

    capture_screenshot(
        context.driver,
        "product_removed"
    )


# ==================================================
# VERIFY CART ITEMS
# ==================================================

@then("the cart should contain added products")
def step_verify_cart(context):

    # context.cart_page.verify_cart_has_items()
    context.product_page.verify_product_added()


# ==================================================
# VERIFY CHECKOUT PAGE
# ==================================================

@then("the checkout page should be displayed")
def step_checkout_page(context):

    assert (
        "checkout"
        in context.driver.current_url.lower()
    )