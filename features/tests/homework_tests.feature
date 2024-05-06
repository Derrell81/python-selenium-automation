# Created by anthony at 4/25/24
Feature: Tests for product page


  Scenario: User can select colors
    Given Open target product A-54551690 page
    Then Verify user can select through colors


  Scenario: Logged out User can access Sign In
    Given Open Target main Page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened
