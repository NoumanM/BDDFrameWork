from Elements.DashboardPageElements import DashboardPageElements
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.common.keys import Keys


class DashboardPage(DashboardPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_progress_bar(self):
        self.verify_element_display(self.progress_bar)

    def verify_weekly_points(self):
        self.verify_element_display(self.weekly_points)

    def verify_tracking_week(self):
        self.verify_element_display(self.tracking_week)

    def click_on_tracking_week(self):
        self.click_element(self.tracking_week)

    def verify_tracking_week_day_picker(self):
        self.verify_element_display(self.tracking_week_day_picker)

    def verify_weekScore_weekDaysAvg_weekEndAvg_progress_bar(self):
        elements_list = self.get_web_elements(self.weekScore_weekDaysAvg_weekEndAvg_progress_bar)
        if len(elements_list) == 3:
            return True

    def verify_modify_view_with_eye_icon(self):
        self.verify_element_display(self.modify_view_with_eye_icon)

    def verify_daily_score_all_areas_chart(self):
        self.verify_element_display(self.daily_score_all_areas_chart)

    def verify_daily_score_all_area_dropdown(self):
        self.verify_element_display(self.daily_score_all_area_dropdown)

    def click_on_daily_score_all_area_dropdown(self):
        self.click_element(self.daily_score_all_area_dropdown)

    def verify_daily_score_all_area_dropdown_options(self):
        self.wait(3)
        elements_list = self.get_web_elements(self.daily_score_all_area_dropdown_options)
        all_options = []
        for el in elements_list:
            all_options.append(el.text)
        return all_options

    def verify_add_new_button_dropdown_options(self):
        self.wait(3)
        elements_list = self.get_web_elements(self.add_new_button_dropdown_options)
        all_options = []
        for i in range(0, len(elements_list)):
            all_options.append((elements_list[i]).text)
        return all_options

    def verify_activity_journal(self):
        self.verify_element_display(self.activity_journal)

    def verify_quote_of_the_day(self):
        self.verify_element_display(self.quote_of_the_day)

    def verify_add_new_button_under_tracking_week(self):
        self.verify_element_display(self.add_new_button_under_tracking_week)

    def click_on_add_new_button_under_tracking_week(self):
        self.click_element(self.add_new_button_under_tracking_week)

    def click_on_modify_view_with_eye_icon(self):
        self.click_element(self.modify_view_with_eye_icon)

    def verify_display_data_label_and_daily_progress_label(self):
        self.verify_element_display(self.display_data_label)
        self.verify_element_display(self.daily_progress_label)

    def verify_field_against_display_data_button_and_field_against_daily_progress_button(self):
        self.verify_element_display(self.field_against_display_data_button)
        self.verify_element_display(self.radio_btn_against_daily_progress)

    def verify_collapse_all_button_and_expand_all_button_on_modify_view(self):
        self.verify_element_display(self.collapse_all_button_on_modify_view)
        self.verify_element_display(self.expand_all_button_on_modify_view)

    def click_on_field_against_display_data_label(self):
        self.click_element(self.field_against_display_data_button)

    def verify_options_against_display_data_label(self):
        self.wait(3)
        elements_list = self.get_web_elements(self.options_against_display_data_label)
        all_options = []
        for i in range(0, len(elements_list)):
            all_options.append((elements_list[i]).text)
        return all_options

    def click_on_radio_btn_against_daily_progress(self):
        try:
            self.click_using_js(self.radio_btn_against_daily_progress)
        except:
            self.wait(2)
            self.driver.execute_script('document.querySelector("#custom-switch").click()')

    def verify_daily_progress_label_on_dashboard(self):
        return self.verify_element_not_display(self.daily_progress_label_on_dashboard)

    def click_on_collapse_all_button_on_modify_view(self):
        self.click_element(self.collapse_all_button_on_modify_view)

    def verify_collapse_all_button_on_modify_view_is_disabled(self):
        return self.verify_element_disabled(self.collapse_all_button_on_modify_view)

    def click_on_expand_all_button_on_modify_view(self):
        self.click_element(self.expand_all_button_on_modify_view)

    def verify_expand_all_button_on_modify_view_is_disabled(self):
        return self.verify_element_disabled(self.expand_all_button_on_modify_view)

    def verify_nutrition_flexibility_headache_weight_subdropables_under_health_is_not_displaying(self):
        return self.verify_element_not_display(self.nutrition_flexibility_headache_weight_subdropables_under_health)

    def verify_add_new_category_popup_window(self):
        try:
            val = self.verify_element_display(self.add_new_category_popup_window)
            return val
        except:
            return False

    def click_on_category_btn(self):
        self.click_element(self.category_btn)

    def click_on_subCategory_btn(self):
        self.click_element(self.subCategory_btn)

    def verify_add_new_subCategory_popup_window(self):
        try:
            return self.verify_element_display(self.add_new_subCategory_popup_window)
        except:
            return False

    def click_on_habit_btn(self):
        self.click_element(self.habit_btn)

    def verify_add_new_habit_popup_window(self):
        try:
            return self.verify_element_display(self.add_new_habit_popup_window)
        except:
            return False

    def click_on_cancel_btn_on_popup_window(self):
        self.click_element(self.cancel_btn_on_popup_window)

    def click_on_x_icon_on_popup_window(self):
        self.click_element(self.x_icon_on_popup_window)

    def click_plus_button_against_todate_in_activity_journal(self):
        self.click_element(self.plus_button_against_todate_in_activity_journal)

    def verify_add_new_note_popup_window(self):
        try:
            self.verify_element_display(self.add_new_note_popup_window)
        except:
            return False

    def click_profile_icon_on_dashboard_page(self):
        self.click_element(self.profile_icon_on_dashboard_page)

    def verify_personal_information_label(self):
        self.verify_element_display(self.personal_information_label)

    def verify_contact_information_label(self):
        self.verify_element_display(self.contact_information_label)

    def verify_login_information_label(self):
        self.verify_element_display(self.login_information_label)

    def verify_day_capital_letters_on_activity_journal(self):
        all_letters = []
        elements = self.get_web_elements(self.day_capital_letters_on_activity_journal)
        for el in elements:
            all_letters.append(el.text)

        return all_letters

    def select_location_from_location_input_field_on_add_note_popup_window(self):
        self.click_element(self.location_input_field_on_add_note_popup_window)
        heatlh_anchor_btn = (By.XPATH, "//span[contains(text(),'Health')]/following-sibling::div[@class='card-header']")
        self.click_element(heatlh_anchor_btn)
        health_sub_fields = (By.XPATH, "(//div[@class='collapse show']/div[contains(@class,'card-body')]//div[@class='sc-liaBrn deeAMP']/span[@class='sc-hTtIkV eLkmdQ'])[position()<5]")
        all_fields = self.get_web_elements(health_sub_fields)
        i =randint(0, 3)
        print(i)
        all_fields[i].click()

    def add_note_on_add_a_new_note_popup_window(self, data):
        self.input_element(self.note_text_area, data)

    def click_add_btn_on_add_a_new_note_popup_window(self):
        self.click_element(self.add_btn_on_add_a_new_note)

    def verify_three_dots_btn_on_new_note_activity_journal(self, note, value):
        three_dots_btn_on_new_note_activity_journal = (By.XPATH, f"(//div[contains(text(),'{note}')]/preceding-sibling::div//div[@class='customDropdown']/div)[last()]")
        if value == 'click':
            self.click_element(three_dots_btn_on_new_note_activity_journal)
        else:
            try:
                self.verify_element_display(three_dots_btn_on_new_note_activity_journal)
            except:
                return False

    def verify_edit_note_link_under_three_dots_btn(self, value):
        self.wait(2)
        if value == 'click':
            self.click_element(self.edit_note_link_under_three_dots_btn)
        else:
            try:
                self.verify_element_display(self.edit_note_link_under_three_dots_btn)
            except:
                return False

    def verify_delete_note_link_under_three_dots_btn(self, value):
        self.wait(2)
        self.verify_element_display(self.delete_note_link_under_three_dots_btn)
        if value == 'click':
            self.click_element(self.delete_note_link_under_three_dots_btn)

    def click_save_btn_on_edit_a_note(self):
        self.click_element(self.save_btn_on_edit_a_note)

    def verify_edit_habit_note_popup_window(self):
        self.wait(3)
        try:
            self.verify_element_display(self.edit_habit_note_popup_window)
        except:
            return False

    def verify_please_select_location_message(self):
        self.verify_element_display(self.please_select_location_message)

    def verify_please_enter_note_message(self):
        self.verify_element_display(self.please_enter_note_message)

    def clear_note_field_on_add_a_new_note_popup_window(self):
        element = self.get_web_element(self.note_text_area)
        element.send_keys(Keys.CONTROL, 'A', '\b')

    def verify_delete_note_popup_window(self):
        try:
            self.verify_element_display(self.delete_note_popup_window)
        except:
            return False

    def click_on_delete_btn_on_delete_note_popup_window(self):
        self.click_element(self.delete_btn_on_delete_note_popup_window)

    def click_x_icon_on_delete_popup_window(self):
        self.click_element(self.x_icon_on_delete_popup_window)

    def click_close_button_on_delete_popup_window(self):
        self.click_element(self.close_button_on_delete_popup_window)