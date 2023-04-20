from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AnalyticsPageElements(BasePage):
    analytics_btn_on_left_side = (By.XPATH, "//a[contains(@title,'Analytics')]")
    charts_tab = (By.XPATH, "//a[contains(text(),'Charts')]")
    net_worth_tab = (By.XPATH, "//a[contains(text(),'Net Worth')]")
    stats_tab = (By.XPATH, "//a[contains(text(),'Stats')]")
    net_worth_label = (By.XPATH, "//span[contains(text(),'Net Worth')]")
    area_activity_tracker_label = (By.XPATH, "//div[contains(text(),'Area Activity Tracker')]")
    from_date_input_field_on_net_worth_page = (By.XPATH, "//input[contains(@placeholder,'From')]")
    to_date_input_field_on_net_worth_page = (By.XPATH, "//input[contains(@placeholder,'To')]")
    available_dates_on_calendars = (By.XPATH, "//div[contains(@class,'DayPicker-Day') and @aria-selected='true']")
    balance_as_of_starting_date = (By.XPATH, "(//span[contains(text(),'Balance as of')])[1]/../following-sibling::span[1]")
    balance_as_of_end_date = (By.XPATH, "(//span[contains(text(),'Balance as of')])[2]/../following-sibling::span[1]")
    net_income = (By.XPATH, "//span[contains(text(),'Net Income')]/following-sibling::div/div[1]/span[1]")
    net_returns = (By.XPATH, "//span[contains(text(),'Net returns')]/../following-sibling::div/span[1]")
    row_under_net_worth = (By.XPATH, "//div[contains(@class, 'accordion')]//button//span")
    assets_liabilities_label_1 = (By.XPATH, "(//span[contains(text(), 'Assets / (Liabilities)')])[1]")
    assets_liabilities_label_2 = (By.XPATH, "(//span[contains(text(), 'Assets / (Liabilities)')])[2]")
    gain_loss_label = (By.XPATH, "//span[contains(text(), 'Gain / (Loss)')]")
    returns_label = (By.XPATH, "//span[contains(text(), 'Returns')]")
    export_to_excel_btn = (By.XPATH, "//div[contains(text(), 'Export To Excel')]")
    tracking_week_label_next_and_previous_btns = (By.XPATH, "//div[contains(text(), 'Tracking Week')]/following-sibling::div/button")
    area_comparison = (By.XPATH, "//div[contains(text(), 'Area Comparison')]/../following-sibling::div[1]/div")
    weekly_comparison_chart = (By.XPATH, "//div[contains(text(), 'Weekly Comparison')]/../../following-sibling::div")
    area_activity_tracker = (By.XPATH, "//div[contains(text(), 'Area Activity Tracker')]/../following-sibling::div[position() < 3]")
    date_picker_under_tracking_week = (By.XPATH, "//div[contains(text(), 'Tracking Week')]/following-sibling::div[1]/div/div[2]")
    available_dates_under_tracking_week = (By.XPATH, "(//div[@class='DayPicker-Body']//div[contains(@class,'DayPicker') and @aria-selected='true' and @aria-disabled='false'])[1]/following-sibling::div[1]")
    tracking_year_dropdown = (By.XPATH, "//div[contains(@class,'yrp-picker-text')]")
    start_year_2022 = (By.XPATH, "//span[contains(text(),'Start')]/following-sibling::ul/li[text()='2022']")
    previous_years_from_2022 = (By.XPATH, "//span[contains(text(),'End')]/following-sibling::ul/li[position()>1]")
    modify_view_btn_on_stats = (By.XPATH, "//button[contains(text(),'Modify view')]")
    points_values_infront_of_each_category = (By.XPATH, "//div[text()= 'Points']/ancestor::div[3]/following-sibling::div[@class='accordion']//button/following-sibling::div/div[5]/div/div")


