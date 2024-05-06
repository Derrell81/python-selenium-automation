from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = (By.CSS_SELECTOR, "[class*='styles__StyledHeading']")

    def verify_sign_in_header(self, expected_item):
        actual_text = self.driver.find_element(*self.SIGN_IN_HEADER)
