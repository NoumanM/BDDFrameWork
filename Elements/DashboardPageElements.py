from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class DashboardPageElements(BasePage):
    progress_bar = (By.XPATH, '//div[contains(text(),"Progress")]/following-sibling::div/div[1]')
    weekly_points = (By.XPATH, "//div[contains(text(),'Arootah Points')]/following-sibling::span/span[1]")
    tracking_week = (By.XPATH, "(//div[contains(@class,'DayPicker')])[1]/following-sibling::div")
    tracking_week_day_picker = (By.XPATH, "(//div[contains(@class,'DayPicker-Month')])[1]")
    weekScore_weekDaysAvg_weekEndAvg_progress_bar = (By.XPATH, "//div[contains(text(),'Weekdays Average')]/../following-sibling::div[1] | //div[contains(text(),'Weekend Average')]/../following-sibling::div[1] | //div[contains(text(),'Week Average')]/../following-sibling::div[1]")
    modify_view_with_eye_icon = (By.XPATH, "//button[contains(text(),'Modify view')]")
    daily_score_all_areas_chart = (By.XPATH, "//div[contains(text(),'Daily Score')]/../../following-sibling::div")
    daily_score_all_area_dropdown = (By.XPATH, "//span[contains(text(),'All Areas')]")
    daily_score_all_area_dropdown_options = (By.XPATH, "(//span[text()='All Areas']/ancestor::div)[1]/following-sibling::div[last()]/div[2]/div/div[position()>1]")
    activity_journal = (By.XPATH, "//div[contains(text(),'Activity')]/following-sibling::div")
    quote_of_the_day = (By.XPATH, "//p[contains(text(),'Quote of the day')]/../following-sibling::div")
    add_new_button_under_tracking_week = (By.XPATH, "//div[contains(text(),'Add New')]/../parent::div[@class='customDropdown']")
    display_data_label = (By.XPATH, "//label[contains(text(),'Displayed data')]")
    daily_progress_label = (By.XPATH, "//label[contains(text(),'Daily progress')]")
    field_against_display_data_button = (By.XPATH, "//label[contains(text(),'Displayed data')]/following-sibling::div/div")
    radio_btn_against_daily_progress = (By.XPATH, "//input[contains(@id,'custom-switch')]")
    collapse_all_button_on_modify_view = (By.XPATH, "//span[contains(text(),'Collapse all')]")
    expand_all_button_on_modify_view = (By.XPATH, "//span[contains(text(),'Expand all')]")
    add_new_button_dropdown_options = (By.XPATH, "//a[contains(@class,'dropdown-item')]")
    options_against_display_data_label = (By.XPATH, "//div[contains(@class,'css-9g7j0m-menu')]/div")
    daily_progress_label_on_dashboard = (By.XPATH, "//span[contains(text(),'Daily Progress')]")
    nutrition_flexibility_headache_weight_subdropables_under_health = (By.XPATH, "//span[contains(text(),'Nutrition')] | //span[contains(text(),'Flexibility')] | //span[contains(text(),'headache')] | //span[contains(text(),'Weight Mgmt.')]")
    category_btn = (By.XPATH, "//a[contains(text(),'Category')]")
    add_new_category_popup_window = (By.XPATH, "//div[contains(text(),'Add New Category')]")
    subCategory_btn = (By.XPATH, "//a[contains(text(),'Subcategory')]")
    add_new_subCategory_popup_window = (By.XPATH, "//div[contains(text(),'Add New Subcategory')]")
    habit_btn = (By.XPATH, "//a[contains(text(),'Habit')]")
    add_new_habit_popup_window = (By.XPATH, "//div[contains(text(),'Location')]/../../../preceding-sibling::div/div[contains(text(),'Add New Habit')]")
    x_icon_on_popup_window = (By.XPATH, "//div[contains(text(),'Add new')]/following-sibling::img | //div[contains(text(),'Add New')]/following-sibling::img")
    cancel_btn_on_popup_window = (By.XPATH, "//button[contains(text(),'Cancel')]")
    plus_button_against_todate_in_activity_journal = (By.XPATH, "(//div[contains(text(),'Activity')]/following-sibling::div//button/following-sibling::div/button)[1]")
    add_new_note_popup_window = (By.XPATH, "//div[contains(text(),'Add new note')]")
    profile_icon_on_dashboard_page = (By.XPATH, "(//img[contains(@alt,'profile')])[1]")
    personal_information_label = (By.XPATH, "//div[contains(text(),'Personal information')]")
    contact_information_label = (By.XPATH, "//div[contains(text(),'Contact information')]")
    login_information_label = (By.XPATH, "//div[contains(text(),'Login information')]")
    day_capital_letters_on_activity_journal = (By.XPATH, "//div[contains(text(), 'Activity')]/following-sibling::div//button/div/div[1]")
    location_input_field_on_add_note_popup_window = (By.XPATH, "//input[contains(@placeholder,'Enter location')]")
    note_text_area = (By.XPATH, "//textarea[contains(@placeholder,'Enter note')]")
    add_btn_on_add_a_new_note = (By.XPATH, "//button[contains(text(),'ADD')]")
    edit_note_link_under_three_dots_btn = (By.XPATH, "//a[contains(text(),'Edit note')]")
    delete_note_link_under_three_dots_btn = (By.XPATH, "//a[contains(text(),'Delete note')]")
    save_btn_on_edit_a_note = (By.XPATH, "//button[contains(text(),'SAVE')]")
    edit_habit_note_popup_window = (By.XPATH, "//div[contains(text(),'Edit habit note')]")
    please_select_location_message = (By.XPATH, "//div[contains(text(),'Please select Location')]")
    please_enter_note_message = (By.XPATH, "//div[contains(text(),'Please Enter Note')]")
    delete_note_popup_window = (By.XPATH, "//div[contains(text(),'Delete note')]")
    delete_btn_on_delete_note_popup_window = (By.XPATH, "//button[contains(text(),'Delete Note')]")
    x_icon_on_delete_popup_window = (By.XPATH, "//button[contains(@class,'close')]")
    close_button_on_delete_popup_window = (By.XPATH, "//button[contains(text(),'Close')]")


