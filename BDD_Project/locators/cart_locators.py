from selenium.webdriver.common.by import By


class CartLocators:

    # ==================================================
    # CART BUTTON
    # ==================================================

    CART_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'basket')]"
    )

    # ==================================================
    # CART ITEMS
    # ==================================================

    CART_ITEMS = (
        By.XPATH,
        "//button[contains(text(),'Add')]"
        " | "
        "//div[contains(@class,'items')]"
        " | "
        "//div[contains(@class,'basket-item')]"
        " | "
        "//div[contains(@class,'CartItem')]"
        " | "
        "//a[contains(@href,'product')]"
    )

    # ==================================================
    # PROCEED BUTTON
    # ==================================================

    PROCEED_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed')]"
        " | "
        "//button[contains(text(),'Checkout')]"
    )

    # ==================================================
    # CHECKOUT PAGE
    # ==================================================

    CHECKOUT_PAGE = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )

    DELETE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Delete']"
    )

    # ==================================================
    # CART PRODUCT
    # ==================================================

    CART_PRODUCT = (
        By.XPATH,
        "//h3[contains(text(),'Tata Tea Chakra Gold')]"
    )