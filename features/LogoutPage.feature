@logout
Feature: Validate the logout feature

  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify user should be able to logout from the site successfully
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click profile icon on dashboard page
    Then Click on logout button
    Then Verify user successfully logout
    Then Close the browser