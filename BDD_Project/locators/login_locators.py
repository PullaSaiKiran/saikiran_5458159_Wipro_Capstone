from selenium.webdriver.common.by import By


class LoginLocators:

    # ==========================================
    # LOGIN BUTTON
    # ==========================================

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login/ Sign Up')]"
    )

    # ==========================================
    # MOBILE INPUT
    # ==========================================

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    # ==========================================
    # CONTINUE BUTTON
    # ==========================================

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[text()='Continue']"
    )

    # ==========================================
    # VERIFY BUTTON
    # ==========================================

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[text()='Verify & Continue']"
    )

    # ==========================================
    # INVALID MOBILE POPUP
    # ==========================================

    INVALID_MOBILE_POPUP = (
        By.XPATH,
        "//*[contains(text(),'valid mobile number')]"
    )

    # ==========================================
    # INVALID OTP POPUP
    # ==========================================

    INVALID_OTP_POPUP = (
        By.XPATH,
        "//*[contains(text(),'Please Enter Valid OTP')]"
    )