import datetime
import os
import random

import mysql.connector
from selenium.webdriver.support.select import Select
from Elements.DashboardPageElements import DashboardPageElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.config import TestData
from pages.SignupPage import SignupPage
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.common.keys import Keys
from Elements.AddNewCategoryPageElements import AddNewCategoryPageElements


class AddNewCategoryPage(AddNewCategoryPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def select_area_on_add_new_category_popup_window(self):
        self.click_element(self.dropdown_icon_against_area)
        elements = self.get_web_elements(self.dropable_options_on_add_new_category)
        (elements[randint(0, 9)]).click()

    def select_category_on_add_new_category_popup_window(self, value):
        if value == 'Select':
            self.click_element(self.select_category)
            elements = self.get_web_elements(self.dropable_options_on_add_new_category)
            try:
                el = elements[1]
            except:
                el = elements[0]
            value1 = el.text
            el.click()
            return value1
        if value == 'no':
            self.click_element(self.select_category)
            try:
                elements = self.get_web_elements(self.dropable_options_on_add_new_category)
                if len(elements) > 0:
                    return False
                else:
                    return True
            except:
                return False

        if value == 'all':
            self.click_element(self.select_category)
            try:
                elements = self.get_web_elements(self.dropable_options_on_add_new_category)
                if len(elements) > 0:
                    return True
                else:
                    return True
            except:
                return False

        if value == 'options':
            options_list = []
            self.click_element(self.select_category)
            try:
                elements = self.get_web_elements(self.dropable_options_on_add_new_category)
                for el in elements:
                    options_list.append(el.text)
                return options_list
            except:
                return options_list


    def verify_added_category_under_daily_progress(self, value):
        el = (By.XPATH, f"//span[contains(text(),'{value}')]")
        self.verify_element_display(el)

    def click_add_button(self, val):
        if val == 'click':
            self.click_element(self.add_btn_on_add_a_new_note)
        if val == 'disabled':
            return self.verify_element_disabled(self.add_btn_on_add_a_new_note)
        if val == 'enabled':
            self.verify_element_enable(self.add_btn_on_add_a_new_note)

    def click_dropdown_against_area(self):
        self.click_element(self.dropdown_icon_against_area)

    def verify_select_category_is_disabled(self, val):
        if val == 'disabled':
            self.verify_element_disabled(self.select_category)
        if val == 'click':
            self.click_element(self.select_category)

    def verify_category_weight_dropdown(self, val):
        if val == 'disabled':
            self.verify_element_disabled(self.category_weight_dropdown)

        if val == 'enabled':
            self.verify_element_enable(self.category_weight_dropdown)

    def get_category_weight_value(self):
        text = self.get_element_text(self.category_weight_value)
        if int(text) > 0:
            return True
        else:
            return False

    def sub_category_name_field_functions(self, val, text):
        if val == 'enter':
            self.input_element(self.sub_category_name_field, text)
        if val == 'enabled':
            self.verify_element_enable(self.sub_category_name_field)
        if val == 'disabled':
            self.verify_element_disabled(self.sub_category_name_field)

    def verify_sub_Category(self, value):
        el = (By.XPATH, f"//span[contains(text(),'{value}')]")
        return self.verify_element_display(el)




