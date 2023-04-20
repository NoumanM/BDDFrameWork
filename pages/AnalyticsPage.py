import random
from pathlib import Path
from Elements.AnalyticsPageElements import AnalyticsPageElements
from time import sleep
import os
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class AnalyticsPage(AnalyticsPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_analytics_btn(self):
        self.click_element(self.analytics_btn_on_left_side)

    def verify_net_worth_tab(self):
        self.verify_element_display(self.net_worth_tab)

    def click_net_worth_tab(self):
        self.click_element(self.net_worth_tab)

    def verify_net_worth_label(self):
        self.verify_element_display(self.net_worth_label)

    def verify_charts_tab(self):
        self.verify_element_display(self.charts_tab)

    def click_charts_tab(self):
        self.click_element(self.charts_tab)

    def verify_stats_tab(self):
        self.verify_element_display(self.stats_tab)

    def click_stats_tab(self):
        self.click_element(self.stats_tab)

    def verify_area_activity_tracker_label(self):
        self.verify_element_display(self.area_activity_tracker_label)

    def select_to_and_from_date_on_net_worth_calendar(self):
        self.click_element(self.from_date_input_field_on_net_worth_page)
        sleep(2)
        try:
            elements = self.get_web_elements(self.available_dates_on_calendars)
            elements[0].click()
        except Exception as e:
            print (e)
        sleep(2)
        self.click_element(self.to_date_input_field_on_net_worth_page)
        sleep(2)
        elements = self.get_web_elements(self.available_dates_on_calendars)
        elements[0].click()

    def verify_balance_as_of_starting_date(self):
        self.verify_element_display(self.balance_as_of_starting_date)

    def verify_balance_as_of_end_date(self):
        self.verify_element_display(self.balance_as_of_end_date)

    def verify_net_income(self):
        self.verify_element_display(self.net_income)

    def verify_net_returns(self):
        self.verify_element_display(self.net_returns)

    def get_row_under_net_worth(self):
        all_names = []
        elements = self.get_web_elements(self.row_under_net_worth)
        for el in elements:
            all_names.append(el.text)
        return all_names

    def verify_asset_liabilities_gain_loss_and_return_labels(self):
        self.verify_element_display(self.assets_liabilities_label_1)
        self.verify_element_display(self.assets_liabilities_label_2)
        self.verify_element_display(self.gain_loss_label)
        self.verify_element_display(self.returns_label)

    def click_export_to_excel_btn(self):
        self.click_element(self.export_to_excel_btn)
        sleep(5)

    def verify_export_to_excel_btn(self):
        self.verify_element_display(self.export_to_excel_btn)

    def verify_file_exist_or_not(self):
        testData = f"{Path(__file__).resolve().parent.parent}\TestData\Download.xlsx"
        return os.path.exists(testData)



    def delete_the_download_file(self):
        testData = f"{Path(__file__).resolve().parent.parent}\TestData\Download.xlsx"
        if os.path.exists(testData):
            os.remove(testData)

    def verify_tracking_week_label_next_and_previous_btns(self):
        self.verify_element_display(self.tracking_week_label_next_and_previous_btns)

    def verify_area_comparison_chart(self):
        self.verify_element_display(self.area_comparison)

    def verify_weekly_comparison_chart(self):
        self.verify_element_display(self.weekly_comparison_chart)

    def verify_area_activity_tracker(self):
        self.verify_element_display(self.area_activity_tracker)

    def click_date_picker_under_tracking_week(self):
        self.click_element(self.date_picker_under_tracking_week)
        sleep(3)
        try:
            self.click_using_js(self.available_dates_under_tracking_week)
        except Exception as e:
            print('Exception Message: '+e)

    def click_tracking_year_dropdown(self):
        self.click_element(self.tracking_year_dropdown)

    def click_start_year_2022(self):
        self.click_element(self.start_year_2022)

    def verify_previous_years_are_disabled(self):
        self.click_tracking_year_dropdown()
        flag = False
        elements = self.get_web_elements(self.previous_years_from_2022)
        try:
            for el in elements:
                if el.is_enabled:
                    flag = False
                    break
                else:
                    flag = True
            return flag
        except:
            return flag


    def verify_element_color(self):
        rgb = self.driver.find_element(By.XPATH, "(//li[contains(@class,'selected')])[1]").value_of_css_property('background-color')

        r, g, b, a = map(int, re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+),\s(\d*)', rgb).groups())
        color = '#%02x%02x%02x%02x' % (r, g, b, a)
        return color

    def verify_modify_view_btn_on_stats(self):
        self.verify_element_display(self.modify_view_btn_on_stats)

    def verify_color_after_hovering_over_modify_view(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, "//button[contains(text(),'Modify view')]")
        action.move_to_element(element).perform()
        sleep(2)
        rgb = self.driver.find_element(By.XPATH, "//button[contains(text(),'Modify view')]").value_of_css_property(
            'background-color')

        r, g, b, a = map(int, re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+),\s(\d*)', rgb).groups())
        color = '#%02x%02x%02x%02x' % (r, g, b, a)
        return color

    def get_points_infront_of_each_category(self):
        all_points = []
        elements = self.get_web_elements(self.points_values_infront_of_each_category)
        for el in elements:
            all_points.append(el.text)

        return all_points

