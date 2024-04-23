from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_EMPTY_HEADER = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div[class*='jfZcrh']")
ADD_TO_CART_BUTTON_SIDE_NAVIGATION = (By.CSS_SELECTOR, 'button[class*="ButtonPrimary-sc-5fh6rr-0 hCWYcY bEdlr"]')
VIEW_TO_CART_BUTTON = (By.CSS_SELECTOR, "a[class*='ButtonSecondary-sc-125aivg-0 hCWYcY bxLMor']")
PRICE_AND_QUANTITY = (By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan']")


@then("Verify 'Your Cart is Empty' message is shown")
def verify_cart(context):
    cart_empty_header = context.driver.find_element(*CART_EMPTY_HEADER).text
    expected_text = "Your cart is empty"
    assert expected_text, f"Expected {expected_text}, but got something different."


@then("Click on Add to cart button")
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(4)


@then("Click on Add to cart button from side navigation")
def add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON_SIDE_NAVIGATION).click()


@then("Click on view cart button")
def view_cart_button(context):
    context.driver.find_element(*VIEW_TO_CART_BUTTON).click()


@then("Verify cart shows {expected_amount} and {item}")
def verify_cart_price_item(context, expected_amount, item):
    expected_amount = float(expected_amount)
    context.driver.find_element(*PRICE_AND_QUANTITY)
