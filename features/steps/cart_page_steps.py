from selenium.webdriver.common.by import By
from behave import given, when, then

CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@then('Verify cart has correct {product_name}')
def verify_product_name(context, product_name):
    context.app.cart_page.verify_product_name(product_name)


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty.message()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.cart_page.click_add_to_cart()


@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart_page()
