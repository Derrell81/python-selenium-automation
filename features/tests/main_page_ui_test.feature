# Created by anthony at 4/23/24
Feature: Tests for main page UI
  # Enter feature description here

  Scenario: Verify header is shown
    Given Open Target main Page
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open Target main Page
    Then Verify header has 6 links

    # Enter steps here