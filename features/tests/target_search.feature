# Created by anthony at 4/6/24
Feature: Search tests
  # Enter feature description here

  Scenario: User can search for tea
    Given Open Target main Page
    When Search for tea
    Then Verify search results are shown for tea


  Scenario: User can search for mug
    Given Open Target main Page
    When Search for mug
    Then Verify search results are shown for mug


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
      | item   | expected_item |
      | coffee | coffee        |
      | tea    | tea           |

