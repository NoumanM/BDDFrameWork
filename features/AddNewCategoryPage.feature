@addNewCategory(DashBoard)
Feature: Validate the Add New Category feature on Dashboard

  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify that user is able to add new category on Dashboard page
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then "Select" category on add new category popup window
    Then Add button on add new category popup window "click"
    Then Verify added category and add new category popup window
    Then Close the browser

  Scenario: Verify that "Select category*" label is inactive when "Area*" is not selected against "Add New Category" popup window
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Click dropdown icon against area
    Then select category dropdown "disabled"
    Then Close the browser

  Scenario: Verify that no list of options is displayed on clicking field against "Select category" when "Area" is not selected
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then select category dropdown "click"
    Then verify "no" list of options displaying
    Then Close the browser

  Scenario: Verify that "Select category*" label becomes active when "Area*" is selected against "Add New Category" popup window
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then select category dropdown "click"
    Then verify "all" list of options displaying
    Then Close the browser

  Scenario: Verify that list of options is displayed on clicking field against "Select category" when "Area" is selected
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then select category dropdown "click"
    Then verify "options" list of options displaying
    Then Close the browser

  Scenario: Verify that "Category weight" label and its value is inactive when no category is selected against "Select category*" field
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then verify category weight dropdown "disabled"
    Then Close the browser

  Scenario: Verify that "Category weight" label and its value becomes active when category is selected against "Select category*" field
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then "Select" category on add new category popup window
    Then verify category weight dropdown "enabled"
    Then Close the browser

  Scenario: Verify that "Category weight" label is shown inactive along empty field when no area is selected
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then verify category weight dropdown "disabled"
    Then Close the browser

  Scenario: Verify that value is selected and shown automatically in the "Category weight" field when area is selected
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then verify category weight value
    Then Close the browser

  Scenario: Verify that "Add" button is shown disable when no category is selected against "Add New Category" popup window
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then Add button on add new category popup window "disabled"
    Then Close the browser

  Scenario: Verify that "Add" button is shown enable when some category is selected against "Add New Category" popup window
    Then Login with valid email and password
    Then Click on category button under Add new button
    Then Select option against area against area
    Then "Select" category on add new category popup window
    Then Add button on add new category popup window "enabled"
    Then Close the browser

  Scenario: Verify that user is able to add new Subcategory on Dashboard Page
    Then Login with valid email and password
    Then Click on sub category button under Add new button
    Then Select option against area against area
    Then "Select" category on add new category popup window
    Then Sub category name field "enter"
    Then Add button on add new category popup window "click"
    Then Verify sub category on dashboard
    Then Close the browser


  Scenario: Verify that "Category*" label is inactive when "Area*" is not selected against "Add New Subcategory" popup window
    Then Login with valid email and password
    Then Click on sub category button under Add new button
    Then select category dropdown "disabled"
    Then Close the browser

  Scenario: Verify that no list of options is displayed on clicking field against "Category" when "Area" is not selected
    Then Login with valid email and password
    Then Click on sub category button under Add new button
    Then select category dropdown "click"
    Then verify "no" list of options displaying
    Then Close the browser

  Scenario: Verify that "Category*" label becomes active when "Area*" is selected against "Add New Subcategory" popup window
    Then Login with valid email and password
    Then Click on sub category button under Add new button
    Then Select option against area against area
    Then select category dropdown "click"
    Then verify "all" list of options displaying
    Then Close the browser


  Scenario: Verify that list of options is displayed on clicking field against "Category*" when "Area" is selected
    Then Login with valid email and password
    Then Click on sub category button under Add new button
    Then Select option against area against area
    Then select category dropdown "click"
    Then verify "options" list of options displaying
    Then Close the browser