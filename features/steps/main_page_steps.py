from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


@given('Open Target main Page')
def open_target(context):
    context.app.main_page.open_main()


@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


# always clicks on 1st Add to cart btn
# Add multiple:
# add_cart_btns = context.driver.find_elements(*ADD_TO_CART_BTN)
# for btn in add_cart_btns[:5]:
#     btn.click() # => will click on the first 5 buttons 1 by 1
# add_cart_btns[4].click() # => will only click on the 5th Add to cart btn


@then("Verify header is shown")
def verify_header_shown(context):
    context.app.search_result_page.verify_search_results


@then("Verify header has {expected_amount} links")
def verify_header_links(context, expected_amount):  # expected_amount = '5'
    expected_amount = int(expected_amount)  # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
    # to print all names:
    # for link in links:
    #     print(link.text)
    # all_text = [link.text for link in links]
    # print(all_text)
