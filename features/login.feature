@login
Feature: Validate the login feature
  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify that user is by default landed on "Login" page when application is accessed
    Then Verify login label is displayed
    Then Close the browser


  Scenario: Verify that user is able to see "Login" button on "Signup" page
    Then Verify Sign up button is displaying
    Then Click Sign up button
    Then Verify register a new account label
    Then Verify login button on signup page
    Then Close the browser

  Scenario: Verify that "Login" button is clickable on "Signup" page
    Then Verify Sign up button is displaying
    Then Click Sign up button
    Then Verify register a new account label
    Then Verify login button on signup page
    Then Click login button
    Then Verify login label is displayed
    Then Close the browser

  Scenario: Verify that user is able to login successfully via valid email and correct password
      Then Login with valid email and password
      Then Verify Habit Accountability Tracking logo is displaying
      Then Close the browser

  Scenario: Verify that user is able to see other "Login" options too on "Login" page
      Then Verify google icon and sigin with other accounts label
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Login" button when "Email" field is left empty
      Then Enter password and click login button
      Then Verify please provide a valid email message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Login" button when invalid "Email" is entered
      Then Enter an invalid email address
      Then Enter password and click login button
      Then Verify please provide a valid email message
      Then Close the browser

  Scenario: Verify that user is not able to login successfully when both "Email" and "Password" fields are empty
      Then Click login button
      Then Verify please provide a valid email message
      Then Verify please provide password message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Login" button when invalid password is entered
      Then Enter valid login email "ambreeny4191+123@gmail.com"
      Then Enter invalid login password "Tes"
      Then Click login button
      Then Verify unable to login with provided credentials message
      Then Close the browser

  Scenario: Verify that user is not able to login successfully when incorrect "Email" and incorrect "Password" is entered
      Then Enter valid login email "ambreeny4191+123@gmail.com"
      Then Enter invalid login password "Test#1234"
      Then Click login button
      Then Verify unable to login with provided credentials message
      Then Close the browser