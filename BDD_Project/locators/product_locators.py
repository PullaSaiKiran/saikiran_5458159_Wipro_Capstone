from selenium.webdriver.common.by import By


class ProductLocators:

    # ==================================================
    # TEA FILTER
    # ==================================================

    EXOTIC_TEA_FILTER = (
        By.XPATH,
        "//a[@href='/pc/beverages/tea/exotic-flavoured-tea/?nc=ct-fa']"
    )

    # ==================================================
    # TEA BRAND
    # ==================================================

    BRAND_CHAI_POINT = (
        By.XPATH,
        "//label[@for='i-ChaiPoint']"
    )

    # ==================================================
    # GHEE CATEGORY
    # ==================================================

    GHEE_VANASPATI = (
        By.XPATH,
        "//a[normalize-space()='Ghee & Vanaspati']"
    )

    # ==================================================
    # GHEE BRAND
    # ==================================================

    BRAND_AMUL = (
        By.XPATH,
        "//label[@for='i-Amul']"
    )

    # ==================================================
    # ADD BUTTON
    # ==================================================

    ADD_BUTTON = (
        By.XPATH,
        "(//button[contains(text(),'Add')])[1]"
    )
    INCREMENT_BUTTON = (
        By.XPATH,
        "(//button[contains(@class,'increment')])[1]"
    )

    # ==========================================
    # BRAND SEARCH BOX
    # ==========================================

    BRAND_SEARCH_BOX = (
        By.CSS_SELECTOR,
        "input[type='text'][placeholder='Search here']"
    )

    # ==========================================
    # TATA TEA CHECKBOX
    # ==========================================

    TATA_TEA_CHECKBOX = (
        By.ID,
        "i-TataTeaChakraGold"
    )

    FILTERED_PRODUCT = (
        By.XPATH,
        "//span[text()='Tata Tea Chakra Gold']"
    )

    # ==========================================
    # PRODUCT QUANTITY
    # ==========================================

    PRODUCT_QUANTITY = (
        By.XPATH,
        "//span[text()='1' or text()='2' or text()='3']"
    )

    # ==========================================
    # GHEE PRODUCT
    # ==========================================

    GHEE_PRODUCT = (
        By.XPATH,
        "//a[contains(@href,'ghee')]"
    )

    # ==========================================
    # RELEVANCE DROPDOWN
    # ==========================================

    RELEVANCE_DROPDOWN = (
        By.XPATH,
        "//button[@aria-haspopup='listbox']"
    )
    # ==========================================
    # PRICE LOW TO HIGH OPTION
    # ==========================================

    PRICE_LOW_TO_HIGH = (
        By.XPATH,
        "//span[text()='Price - Low to High']"
    )

    # ==========================================
    # SORTED GHEE PRODUCT
    # ==========================================

    SORTED_GHEE_PRODUCT = (
        By.XPATH,
        "//h3[contains(text(),'Ghee')]"
    )
    # ==========================================
    # NO RESULTS MESSAGE
    # ==========================================

    NO_RESULTS_FOUND = (
        By.XPATH,
        "//span[text()='No results found']"
    )
