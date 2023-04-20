@Analytics
Feature: Validate the Analytics feature

  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify user should be able to see three tab button on the top left of the analytics page
    Then Login with valid email and password
    Then Click analytics button
    Then Verify charts, net worth, stats tab on analytics page
    Then Close the browser

  Scenario: Verify user should be able to see net worth page by clicking on the button with label "Net worth" on the analytics page
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Verify net worth label
    Then Close the browser


  Scenario: Verify user should be able to see charts page by clicking on the button with label "Charts" on the analytics page
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Verify area activity tracker label
    Then Close the browser


  Scenario: Verify user should be able to select time period by enabled dates on the calendar
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Select date on net worth page to and from
    Then Close the browser

  Scenario: Verify user should be able to see the net worth row with all details
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Verify balance as of starting date, ending date, Net Income and Net Returns
    Then Close the browser

  Scenario: Verify user should be able to see all categories with expand option under the net worth row
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Verify the row names under net worth
    Then Close the browser

  Scenario: Verify user should be able to see details infront of each category
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Verify asset liabilities gain/loss and returns label
    Then Close the browser

  Scenario: Verify user should be able to export all analytics by net worth in xlsx file
    Then Login with valid email and password
    Then Click analytics button
    Then Click net worth tab
    Then Click export to excel button
    Then Verify the download file
    Then Close the browser

  Scenario: Verify user should be able to see the tracking week on the top left corner of the charts screen
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Verify tracking week label, next and previous button
    Then Close the browser

  Scenario: Verify user should be able to see "area comparison" chart on the right side of the screen
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Verify area comparison chart
    Then Close the browser


  Scenario: Verify user should be able to see "Weekly comparison" chart of the right bottom of the screen
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Verify weekly comparison chart
    Then Close the browser

  Scenario: Verify user should be able to see "Area tracker activity" below the tracker week
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Verify area activity tracker and elements under it
    Then Close the browser

  Scenario: Verify user should be able to select any date from the current selected week from the Area activity tracker
    Then Login with valid email and password
    Then Click analytics button
    Then Click charts tab
    Then Click date picker under tracking week
    Then Close the browser

  Scenario: Verify user should be able to see stats page by clicking on the button with label "Stats" on the analytics page
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Verify net worth label
    Then Close the browser

  Scenario: Verify user should not be able to select the end year less than start year from the tracking years dropdown
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Click tracking year dropdown
    Then Click start year 2022
    Then Verify previous years are disabled
    Then Close the browser

  Scenario: Verify that the selected years from the tracking years dropdown is showing highlighted
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Click tracking year dropdown
    Then Click start year 2022
    Then Verify element color
    Then Close the browser

  Scenario: Verify that the years which can not be selected are disabled
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Click tracking year dropdown
    Then Click start year 2022
    Then Verify element color
    Then Close the browser

  Scenario: Verify user should be able to see two button on the top right of the stats page
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Verify modify view and export to excel button
    Then Close the browser

  Scenario: Verify user should be able to see all categories with expand option in the stats section under the tracking year dropdown
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Verify the row names under stats
    Then Close the browser


  Scenario: Verify user should be able to export stats in xlsx file
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Click export to excel button
    Then Verify the download file
    Then Close the browser

  Scenario: Verify the "Modify view" changes its color on hovering
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Verify the color of modify view button after hovering
    Then Close the browser

  Scenario: Verify user is able to see "Points" column at the most right on stats infront of all categories
    Then Login with valid email and password
    Then Click analytics button
    Then Click Stats tab
    Then Verify the points infront of each category
    Then Close the browser