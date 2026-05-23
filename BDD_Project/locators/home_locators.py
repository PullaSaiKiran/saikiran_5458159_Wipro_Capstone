from selenium.webdriver.common.by import By


class HomeLocators:

    # ==================================================
    # TEA CATEGORY
    # ==================================================

    TEA_MENU = (
        By.XPATH,
        "//a[contains(@href,'tea')]"
    )

    # ==================================================
    # GHEE CATEGORY
    # ==================================================

    GHEE_CATEGORY = (
        By.XPATH,
        "//a[contains(@href,'ghee')]"
    )

    # ==================================================
    # BASKET BUTTON
    # ==================================================

    BASKET_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'basket')]"
    )

    # ==================================================
    # CHECKOUT BUTTON
    # ==================================================

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )