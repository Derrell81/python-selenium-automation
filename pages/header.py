from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then



class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")


    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)


    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)