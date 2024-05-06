from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_BTN = (By.CSS_SELECTOR, '[class*="LinkText-sc-1e1g60c-3"]')
SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_HEADER = (By.CSS_SELECTOR, "[class*='styles__StyledHeading']")


@when('Click Sign In')
def click_sign_in_btn(context):
    context.app.header.click_sign_in_btn()
