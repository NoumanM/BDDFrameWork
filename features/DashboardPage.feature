@dashboard
Feature: Validate the Dashboard feature

  Background:
    Given Launch the browser
    When Open the website_url

  Scenario: Verify that user is able to redirect to Dashboard page by default after successful login
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Close the browser

  Scenario: Verify that user is able to see progress bar on "Dashboard" page at top right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify progress bar
    Then Close the browser

  Scenario: Verify that user is able to see "Weekly Points" on "Dashboard" page at top right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify weekly points
    Then Close the browser

  Scenario: Verify that user is able to see "Tracking week" on "Dashboard" page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify tracking week
    Then Close the browser


  Scenario: Verify that Date Picker icon is clickable against "Tracking week" on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click on tracking week date picker
    Then Verify tracking week day picker
    Then Close the browser

  Scenario: Verify that user is able to see progress bars against "Week Score", "Weekdays Avg", "Weekend Avg" on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify week score, week days avg, weekend avg progress bar
    Then Close the browser

  Scenario: Verify that user is able to see "Modify View" button along eye icon on dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Close the browser

  Scenario: Verify that user is able to see "Daily Score" section on dashboard page at right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify daily score all area label and chart
    Then Close the browser

  Scenario: Verify that user is able to see "Daily Score" section on dashboard page at right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify daily score all area dropdown
    Then Close the browser

  Scenario: Verify that dropdown icon is clickable against Daily Score section on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify daily score all area dropdown
    Then Click on daily score all area dropdown
    Then Verify daily score all area dropdown options
    Then Close the browser


  Scenario: Verify that user is able to see "Activity Journal" section on Dashboard page at right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify activity journal
    Then Close the browser

  Scenario: Verify that user is able to see "Quote of the day habits" section on Dashboard page at right side
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify quote of the section
    Then Close the browser

  Scenario:  Verify that user is able to see "+ Add New" button below "Tracking Week" on dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify add new button under tracking week
    Then Close the browser

  Scenario:  Verify that "Modify View" button is clickable on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Verify display data label and daily progress label
    Then Verify field against display data and daily progress label
    Then Verify collapse all and expand all buttons on modify view popup
    Then Close the browser

  Scenario:  Verify that + Add New button is clickable on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Close the browser

  Scenario:  Verify that dropdown icon is clickable against "Displayed data" field on popup window
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Verify display data dropdown options
    Then Close the browser

  Scenario:  Verify that user is able to turn off radio button against Daily progress label
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Click on radio button against daily progress
    Then Verify daily progress label on dashboard
    Then Close the browser

  Scenario:  Verify that user is able to turn on radio button against "Daily progress" label
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Click on radio button against daily progress
    Then Verify daily progress label on dashboard
    Then Close the browser

  Scenario:  Verify that user is able to click on "Collapse all" option on popup window
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Click on collapse all button on modify view
    Then Verify collapse all button is disabled
    Then Verify sub dropables under health "Collapse"
    Then Close the browser

  Scenario:  Verify that user is able to click on "Expand all" option on popup window
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify modify view with icon
    Then Click on modify view with eye icon
    Then Click on collapse all button on modify view
    Then Click on expand all button on modify view
    Then Click on expand all button on modify view is disabled
    Then Verify sub dropables under health "Expand"
    Then Close the browser

  Scenario: Verify that user is able to see "Add New Category" popup window on clicking "Category" option
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on category button and verify add new category popup window
    Then Close the browser

  Scenario: Verify that user is able to see "Add New Sub Category" popup window on clicking "Sub Category" option
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on sub category button and verify add new sub category popup window
    Then Close the browser

  Scenario: Verify that user is able to see "Add New Habit" popup window on clicking "Habit" option
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on habit button and verify add new habit popup window
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Category" popup window on clicking 'X' icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on category button and verify add new category popup window
    Then Click x icon on popup window
    Then Verify the popup window "category"
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Subcategory" popup window on clicking 'X' icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on sub category button and verify add new sub category popup window
    Then Click x icon on popup window
    Then Verify the popup window "sub category"
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Habit" popup window on clicking 'X' icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on habit button and verify add new habit popup window
    Then Click x icon on popup window
    Then Verify the popup window "habit"
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Category" popup window on clicking "Cancel" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on category button and verify add new category popup window
    Then Click cancel button on popup window
    Then Verify the popup window "category"
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Subcategory" popup window on clicking "Cancel" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on sub category button and verify add new sub category popup window
    Then Click cancel button on popup window
    Then Verify the popup window "sub category"
    Then Close the browser

  Scenario: Verify that user is able to close "Add New Habit" popup window on clicking "Cancel" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click add new button and verify dropdown options
    Then Click on habit button and verify add new habit popup window
    Then Click cancel button on popup window
    Then Verify the popup window "habit"
    Then Close the browser

  Scenario: Verify that user is able to click "+" button against a particular date on "Activity Journal" section
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Verify add new note popup window "displaying"
    Then Close the browser

  Scenario: Verify that user is able to close "Add new note" popup window on clicking 'X' icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Verify add new note popup window "displaying"
    Then Click x icon on popup window
    Then Verify add new note popup window "not displaying"
    Then Close the browser

  Scenario: Verify that user is able to close "Add new note" popup window on clicking "Cancel" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Verify add new note popup window "displaying"
    Then Click cancel button on popup window
    Then Verify add new note popup window "not displaying"
    Then Close the browser

  Scenario: Verify that user is able to access profile page on clicking "Profile" icon against "Dashboard" page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click profile icon on dashboard page
    Then Verify information labels on profile page
    Then Close the browser

  Scenario: Verify that user is able to see first Capital letter of Day against "Activity Journal" on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Verify day capital letters on activity journal
    Then Close the browser

  Scenario: Verify that user is able to see "⋮" for newly added note against "Activity Journal" section
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "display"
    Then Close the browser

  Scenario: Verify that user is able to click "⋮" against "Newly added" note under "Activity Journal" section
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "display"
    Then Verify delete note link under three dots button "display"
    Then Close the browser

  Scenario: Verify that user is able to edit a note against "Activity Journal" section on Dashboard page
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Choose location from location input field on add note popup window add note and click on save button
    Then Verify three dots button on new note "display"
    Then Close the browser


  Scenario: Verify that user is able to see "Edit habit note" popup window on clicking "Edit note" option
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Verify edit habit note popup window "displaying"
    Then Close the browser

  Scenario: Verify that user is able to close "Edit habit note" popup window on clicking "X" icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Click x icon on popup window
    Then Verify edit habit note popup window "not displaying"
    Then Close the browser


  Scenario: Verify that user is able to close "Edit habit note" popup window on clicking "Cancel" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Click cancel button on popup window
    Then Verify edit habit note popup window "not displaying"
    Then Close the browser

  Scenario: Verify that "Save" button is clickable against "Edit habit note" popup window
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Click save button on edit a new note popup window
    Then Verify edit habit note popup window "not displaying"
    Then Close the browser

  Scenario: Verify that user is not able to add new note on clicking "Add" button when "Location" field is empty
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Enter add note popup window add note and click on add button
    Then Please select location message "displaying"
    Then Close the browser

  Scenario: Verify that user is not able to add new note on clicking "Add" button when "Note" field is empty
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field and click on add button
    Then Please enter note message "displaying"
    Then Close the browser

  Scenario: Verify that user is not able to edit habit note successfully when Note field is empty
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify edit note link under three dots button "click"
    Then Choose location from location input field, clear note field and click on save button
    Then Please enter note message "displaying"
    Then Close the browser

  Scenario: Verify that user is able to see a "Delete note" popup window on clicking "Delete note" option
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify delete note link under three dots button "click"
    Then Verify delete note pop up "displaying"
    Then Close the browser

  Scenario: Verify that user is able to Close a "Delete note" popup window on clicking "X" icon
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify delete note link under three dots button "click"
    Then Verify delete note pop up "displaying"
    Then Click x icon on delete note pop up window
    Then Verify delete note pop up "not displaying"
    Then Close the browser

  Scenario: Verify that user is able to Close a "Delete note" popup window on clicking "Close" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify delete note link under three dots button "click"
    Then Verify delete note pop up "displaying"
    Then Click close button on delete note pop up window
    Then Verify delete note pop up "not displaying"
    Then Close the browser

  Scenario: Verify that user is able to delete note successfully on clicking "Delete" button
    Then Login with valid email and password
    Then Verify Habit Accountability Tracking logo is displaying
    Then Click plus button against todate in activity journal
    Then Choose location from location input field on add note popup window add note and click on add button
    Then Verify three dots button on new note "click"
    Then Verify delete note link under three dots button "click"
    Then Verify delete note pop up "displaying"
    Then Click delete button on delete note pop up
    Then Verify delete note pop up "not displaying"
    Then Verify three dots button on new note "not displaying"
    Then Close the browser

