import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class GheePage(BasePage):
    GHEE_VANASPATI = (By.XPATH, "//a[normalize-space()='Ghee & Vanaspati']")

    BRAND_AMUL = (By.XPATH, "//label[@for='i-Amul']")

    ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add')]")

    def click_ghee_vanaspati(self):
        element = self.driver.find_element(*self.GHEE_VANASPATI)
        self.driver.execute_script("arguments[0].click();", element)

    def apply_brand_amul(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BRAND_AMUL))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def add_first_product_to_cart(self):
        element = self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Use JS click to avoid interception issues
        self.driver.execute_script("arguments[0].click();", element)


