from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign In form opened')
def verify_sign_in_header(context):
    context.app.sign_in_page.verify_sign_in_header
