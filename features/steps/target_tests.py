from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)
@when('Click on Cart icon')
def click_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then('Verify "Your Cart is Empty" message is shown')
def verify_cart(context):
    cart_empty_header = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    expected_text = "Your cart is empty"
    assert expected_text, f"Expected {expected_text}, but got something different"

@when('Click Sign In')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, '.styles__LinkText-sc-1e1g60c-3.dZfgoT.h-margin-r-x3').click()
    sleep(2)
@then('From right side, navigation menu, click Sign In')
def click_signin_rightside(context):
    context.driver.find_element(By.CSS_SELECTOR, '#listaccountNav-signIn').click()
    sleep(2)

@then('Verify Sign In form opened')
def verify_signin_form(context):
    signin_form_header = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="jhKFiw kcHdEa"]')
    expected_text = "Sign into your Target account"
    assert expected_text, f"Expected {expected_text}, however not found. Test not passed"
