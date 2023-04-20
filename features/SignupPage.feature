@signup
Feature: Validate the signup feature
  Background:
    Given Launch the browser
    When Open the website_url


  Scenario: Verify that user is able to access "Habit Accountability Tracker" site successfully
    Then Verify Habit Accountability Tracking logo is displaying
    Then Close the browser

  Scenario: Verify that user is able to see "Signup" button on Application web page
    Then Verify Sign up button is displaying
    Then Close the browser

  Scenario: Verify that "Signup" button is clickable on Application web page
    Then Verify Sign up button is displaying
    Then Click Sign up button
    Then Close the browser

  Scenario: Verify that user is able to do successful "signup" against "Register new account" page
    Then Verify Sign up button is displaying
    Then Click Sign up button
    When Enter email address on signup page
    When Enter password and confirm password
    When Check i agree checkbox
    Then Click Sign up button
    Then Verify login label is displayed
    Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button when email field is left empty
    Then Verify Sign up button is displaying
    Then Click Sign up button
    When Enter password and confirm password
    When Check i agree checkbox
    Then Click Sign up button
    Then Verify this field may not be empty message
    Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button when password field is left empty
    Then Verify Sign up button is displaying
    Then Click Sign up button
    When Enter email address on signup page
    When Check i agree checkbox
    Then Click Sign up button
    Then Verify this field may not be empty message
    Then Close the browser

    Scenario: Verify that user is able to see a proper validation message on clicking "Signup" button when "password" and "Confirm Password" do not match
      Then Verify Sign up button is displaying
      Then Click Sign up button
      When Enter email address on signup page
      When Enter password
      When Enter confirm password
      When Check i agree checkbox
      Then Click Sign up button
      Then Verify password should be same as confirm password message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button against checkbox  when it is unchecked
      Then Verify Sign up button is displaying
      Then Click Sign up button
      When Enter email address on signup page
      When Enter password and confirm password
      Then Click Sign up button
      Then Verify You must accept our terms of agreement before completing sign up message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button when invalid email is entered
      Then Verify Sign up button is displaying
      Then Click Sign up button
      Then Enter an invalid email address
      When Enter password and confirm password
      When Check i agree checkbox
      Then Click Sign up button
      Then Verify enter a valid email message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button when invalid password is entered
      Then Verify Sign up button is displaying
      Then Click Sign up button
      When Enter email address on signup page
      When Enter invalid password and confirm password
      When Check i agree checkbox
      Then Click Sign up button
      Then Verify invalid password message
      Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Signup" button when password strength is less than 8 characters
      Then Verify Sign up button is displaying
      Then Click Sign up button
      When Enter email address on signup page
      Then Enter password less than 8 characters
      When Check i agree checkbox
      Then Click Sign up button
      Then Verify password length should be minimum 8 characters message
      Then Close the browser

    Scenario: Verify that user is able to see other "Signup" options too on "Register new account" page
      Then Verify Sign up button is displaying
      Then Click Sign up button
      Then Verify register a new account label
      Then Verify google icon and signup with other accounts is displaying
      Then Close the browser

