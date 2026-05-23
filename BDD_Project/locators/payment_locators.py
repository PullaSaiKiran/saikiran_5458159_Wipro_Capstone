from selenium.webdriver.common.by import By


class PaymentLocators:

    # ==========================================
    # CARD NUMBER INPUT
    # ==========================================

    CARD_NUMBER_INPUT = (
        By.NAME,
        "cc-number"
    )

    # ==========================================
    # EXPIRY INPUT
    # ==========================================

    EXPIRY_INPUT = (
        By.NAME,
        "cc-exp"
    )

    # ==========================================
    # INVALID CARD ERROR
    # ==========================================

    INVALID_CARD_ERROR = (
        By.XPATH,
        "//article[@role='none' and "
        "text()='Recheck the card number']"
    )


    PROCEED_TO_CHECKOUT = (
            By.XPATH,
            "//button[contains(text(),'Proceed')]"
        )