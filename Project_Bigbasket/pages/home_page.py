from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    # Tea Category
    TEA_MENU = (
        By.XPATH,
        "//span[text()='Tea']"
    )
    # GHEE_CATEGORY = (By.XPATH, "//span[text()='Ghee']")

    GHEE_CATEGORY= (By.XPATH,
    "//a[contains(@href,'ghee')]"

    )

    # Basket Button
    BASKET_BUTTON = (
        By.XPATH,
        "//a[contains(@href,'basket')]"
    )
    # Proceed To Checkout
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Proceed to Checkout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_tea(self):
        element = self.driver.find_element(*self.TEA_MENU)
        self.driver.execute_script("arguments[0].click();", element)

    def click_ghee(self):
        element = self.driver.find_element(*self.GHEE_CATEGORY)
        self.driver.execute_script("arguments[0].click();", element)


        # Open Basket

    def click_basket(self):
        element = self.wait.until(
            EC.presence_of_element_located(
                self.BASKET_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

        time.sleep(3)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        print("Basket Opened Successfully")

    def click_checkout(self):
        element = self.driver.find_element(*self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
