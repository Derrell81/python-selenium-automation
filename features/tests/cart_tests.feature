Feature: Cart tests

  Scenario: 'Your car is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Verify item is in cart and price is shown
    Given Open Target main Page
    When Search for glass
    Then Click on Add to cart button
    Then Click on Add to cart button from side navigation
    Then Click on view cart button
    Then Verify cart shows 20.99 and item
