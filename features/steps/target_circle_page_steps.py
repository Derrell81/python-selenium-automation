from selenium.webdriver.common.by import By
from behave import given, when, then


BENEFIT_CELLS = (By.CSS_SELECTOR, "[class*='cell-item-content']")


@given('Open Target Circle Page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify page has {expected_amount} benefit cells')
def verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(cells) == expected_amount, f'Expected {expected_amount} cells but got {len(cells)}'