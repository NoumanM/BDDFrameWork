import random
import time

from Elements.ProfilePageElements import ProfilePageElements
from selenium.webdriver.common.by import By
from random import randint
from selenium.webdriver.common.keys import Keys
import os
from Constants.config import TestData
import calendar
from datetime import date
from pathlib import Path


class ProfilePage(ProfilePageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def change_profile_pic(self):
        element = self.get_web_element(self.profile_img_input)
        img = os.getcwd() + f'/TestData/Picture/new{random.randint(1,4)}'
        element.send_keys(img)

    def verify_first_name_input_field(self):
        return self.verify_element_display(self.first_name_input_field)

    def verify_last_name_input_field(self):
        return self.verify_element_display(self.last_name_input_field)

    def verify_email_input_field(self):
        return self.verify_element_display(self.email_input_field)

    def verify_phone_input_field(self):
        return self.verify_element_display(self.phone_input_field)

    def verify_reset_my_password(self):
        return self.verify_element_display(self.reset_my_password)

    def enter_first_name(self):
        self.input_element(self.first_name_input_field, self.generate_random_data_against_a_keyword('firstName'))

    def enter_last_name(self):
        self.input_element(self.last_name_input_field, self.generate_random_data_against_a_keyword('lastName'))

    def click_saveChanges_btn(self):
        self.click_element(self.saveChanges_btn)

    def verify_saved_successfully_msg(self):
        self.verify_element_display(self.saved_successfully)

    def verify_email_input_field_contains_correct_email(self):
        element = self.get_attribute_of_a_element(self.email_input_field, 'value')
        if str(TestData.email) == element:
            return True
        else:
            return False

    def enter_phone_number(self):
        self.input_element(self.phone_input_field, self.generate_random_phone_number())

    def enter_invalid_phone_number(self):
        self.input_element(self.phone_input_field, '00000000000')

    def enter_email_input_field(self):
        self.input_element(self.email_input_field, 'sample@com')

    def verify_invalid_phone_number_msg(self):
        self.verify_element_display(self.invalid_phone_number_msg)

    def verify_invalid_email_address_msg(self):
        self.verify_element_display(self.invalid_email_address_msg)

    def verify_today_and_todate(self):
        combine = str(calendar.month_name[date.today().month]).strip() +" "+ str(date.today().day).strip()
        day = calendar.day_name[date.today().weekday()]
        return self.driver.find_element(By.XPATH, f"//div[contains(text(),'{combine}')]/preceding-sibling::div[text()='{day[0]}']")


    def upload_profile_picture(self):
        testData = f"{Path(__file__).resolve().parent.parent}\TestData\Picture\pic{random.randint(1,4)}.jpg"
        self.driver.execute_script('document.querySelector("input").setAttribute("style", "display:inline")')
        element = self.get_web_element(self.profile_img_input)
        element.send_keys(testData)
        time.sleep(5)