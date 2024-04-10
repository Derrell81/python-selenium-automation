# Created by anthony at 4/6/24
Feature: Target tests
  # Enter feature description here

  Scenario: Verify Cart is Empty
    Given Open Target Page
    When Click on Cart icon
    Then Verify "Your Cart is Empty" message is shown


  Scenario: Verify Logged out user can navigate to Sign In Form
    Given Open Target Page
    When Click Sign In
    Then From right side, navigation menu, click Sign In
    Then Verify Sign In form opened
