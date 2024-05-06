from selenium.webdriver.common.by import By
from behave import given, when, then

SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "#listaccountNav-signIn")


@then('From right side navigation menu, click Sign In')
def side_nav_sign_in_btn(context):
    context.app.side_menu_page.side_nav_sign_in_btn()


@when('Store product name')
def store_product_name(context):
    context.app.side_menu_page.store_product_name()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.side_menu_page.side_nav_add_to_cart_btn()


@then('Click on View Cart & Check Out button')
def view_cart_check_out_btn(context):
    context.app.side_menu_page.view_cart_check_out_btn()
