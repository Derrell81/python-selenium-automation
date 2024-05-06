from pages.base_page import Page

from selenium.webdriver.common.by import By


class CartPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')

    def verify_cart_items(self, amount):
        cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
        assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"

    def verify_product_name(self, product_name):
        cart_item_titles = self.driver.find_element(*self.CART_ITEM_TITLE).text
        found = False
        for cart_item_title in cart_item_titles:
            if product_name in cart_item_title:
                found = True
                break
        assert found, f"Expected {product_name} but got {cart_item_titles}."
