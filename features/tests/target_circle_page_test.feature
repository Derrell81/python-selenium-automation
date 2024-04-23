# Created by anthony at 4/23/24
Feature: Test for target circle page
  # Enter feature description here

  Scenario: Verify page has correct amount of benefit cells
    Given Open Target Circle page
    Then Verify page has 10 benefit cells
