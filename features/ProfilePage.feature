@profile
Feature: Validate the Profile feature

  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify user is able to redirected to the profile page by clicking the profile icon from the left menu bar
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click profile icon on dashboard page
    Then Verify information labels on profile page
    Then Close the browser


  Scenario: Verify user should be able to see profile information on the profile page
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Verify all fields on profile page are displaying
    Then Close the browser

  Scenario: Verify user should be able to set first name and last name
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Enter first name and last name on profile page
    Then Click save changes btn
    Then Verify saved successfully message is displaying
    Then Close the browser

  Scenario: Verify that correct email address is showing when user login through that email
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Verify correct email is displaying
    Then Close the browser

  Scenario: Verify user should be able to set phone number
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Enter a phone number
    Then Click save changes btn
    Then Verify saved successfully message is displaying
    Then Close the browser

  Scenario: Verify validation message appears when user trying to save invalid phone number
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Enter a invalid phone number
    Then Click save changes btn
    Then Verify a invalid phone number message
    Then Close the browser

  Scenario: Verify validation message appears when user trying to save invalid email address
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Enter a invalid email address
    Then Click save changes btn
    Then Verify a invalid email address message
    Then Close the browser

  Scenario: Verify user should be able to see activity week dates on the right corner of the screen with the today's date as active
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Verify day, month and date on left side of profile page
    Then Close the browser

  Scenario: Verify user should be able to upload his/her picture from the profile page
    Then Login with valid email and password
    Then Click on Profile Icon
    Then Upload profile picture
    Then Close the browser