from behave import when, then

from pages.payment_page import (
    PaymentPage
)

from utils.screenshot import (
    capture_screenshot
)

from utils.excel_reader import (
    ExcelReader
)


# ==================================================
# ENTER INVALID CARD NUMBER
# ==================================================

@when("the user enters invalid card number")
def step_invalid_card(context):

    invalid_card = ExcelReader.get_data(
        "data/test_data.xlsx",
        "Sheet1",
        2,
        5
    )

    context.payment_page = PaymentPage(
        context.driver
    )

    context.payment_page.enter_invalid_card_number(
        invalid_card
    )

    capture_screenshot(
        context.driver,
        "invalid_card_entered"
    )


# ==================================================
# VERIFY INVALID CARD ERROR
# ==================================================

@then("invalid card error should be displayed")
def step_invalid_card_error(context):

    context.payment_page.verify_invalid_card_error()

    capture_screenshot(
        context.driver,
        "invalid_card_error"
    )

# ==================================================
# CLICK PROCEED TO CHECKOUT
# ==================================================
@when("the user clicks on Proceed to Checkout")
def step_checkout(context):

    context.payment_page = PaymentPage(
        context.driver
    )

    context.payment_page.click_proceed_to_checkout()