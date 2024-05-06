Feature: Cart tests

  Scenario: 'Your car is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    Then Click on View Cart & Check Out button
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
