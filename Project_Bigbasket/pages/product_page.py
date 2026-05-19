import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):

    # Exotic & Flavoured Tea
    EXOTIC_TEA_FILTER = (
        By.XPATH,
        "//a[@href='/pc/beverages/tea/exotic-flavoured-tea/?nc=ct-fa']"
    )

    # Brand Amul
    BRAND_CHAI_POINT = (By.XPATH, "//label[@for='i-ChaiPoint']")


    # First Product Add to Cart
    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add')]")

    # Increment Button
    # INCREMENT_BUTTON = (
    #     By.XPATH,
    #     "//button[@id='increment']"
    # )

    # --- Methods ---
    def filter_exotic_tea(self):
        element = self.wait.until(EC.element_to_be_clickable(self.EXOTIC_TEA_FILTER))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def apply_brand_chai_point(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BRAND_CHAI_POINT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def add_first_product_to_cart(self):
        element = self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Use JS click to avoid interception issues
        self.driver.execute_script("arguments[0].click();", element)

        # Increase Quantity

    # def click_increment(self):
    #     element = self.driver.find_element(*self.INCREMENT_BUTTON)
    #
    #     self.driver.execute_script(
    #         "arguments[0].click();",
    #         element
    #     )
