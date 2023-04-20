@forgetpassword
Feature: Validate the forget password feature
  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify that user is able to see "I forgot my password" link on "Login" page
    Then Verify i forget my password link
    Then Close the browser

  Scenario: Verify that user is able to see "I forgot my password" link on "Signup" page
    Then Click Sign up button
    Then Verify i forget my password link
    Then Close the browser

  Scenario: Verify that user is able to access "Forgot Password" page on clicking "I forgot my password" link from "Login" page
    Then Click on i forget my password link
    Then Verify forget password label
    Then Close the browser

  Scenario: Verify that user is able to access "Forgot Password" page on clicking "I forgot my password" link from "Signup" page
    Then Click Sign up button
    Then Click on i forget my password link
    Then Verify forget password label
    Then Close the browser

  Scenario: Verify that user is able to see successful notification for reset password on clicking "Reset my password" button
    Then Click on i forget my password link
    Then Enter valid login email "ambreeny4191+123@gmail.com"
    Then Click on reset password button
    Then Verify An email has been sent to provided email address message
    Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Reset my password" button when "Email" field is left empty
    Then Click on i forget my password link
    Then Click on reset password button
    Then Verify please provide a valid email message
    Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Reset my password" button when invalid email address is entered in "Email" field
    Then Click on i forget my password link
    Then Enter an invalid email address
    Then Click on reset password button
    Then Verify please provide a valid email message
    Then Close the browser

  Scenario: Verify that user is able to see a validation message on clicking "Reset my password" button when unregsitered email address is entered in "Email" field
    Then Click on i forget my password link
    Then Enter unregister email address
    Then Click on reset password button
    Then Verify please provide a valid email message
    Then Close the browser