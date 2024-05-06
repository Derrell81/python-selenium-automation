from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SideMenuPage(Page):
    SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "#listaccountNav-signIn")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".styles__ThreeUpButtonWrapper-sc-11rka0i-0.gfFifD")
    VIEW_CART_BTN = (By.XPATH, "//a[text()='View cart & check out']")

    def side_nav_sign_in_btn(self):
        self.click(*self.SIDE_NAV_SIGN_IN_BTN)

    def store_product_name(self, *SIDE_NAV_PRODUCT_NAME):
        self.wait.until(
            EC.presence_of_element_located(self.SIDE_NAV_PRODUCT_NAME),
            message='Product name not present on the page'
        )
        self.product_name = self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

    def side_nav_add_to_cart_btn(self):
        self.click(*self.SIDE_NAV_ADD_TO_CART_BTN)

    def view_cart_check_out_btn(self):
        self.click(*self.VIEW_CART_BTN)
