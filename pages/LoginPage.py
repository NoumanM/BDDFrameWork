import datetime
import os
import mysql.connector
from selenium.webdriver.support.select import Select
from Elements.LoginPageElements import LoginPageElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.config import TestData
from pages.SignupPage import SignupPage


class LoginPage(LoginPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_login_label_is_displayed(self):
        self.verify_element_display(self.login_label)

    def verify_login_button_on_signup_page(self):
        self.verify_element_display(self.login_button)

    def click_login_button(self):
        self.click_element(self.login_button)

    def enter_email_input_field_on_login_page(self, email):
        self.input_element(self.email_input_field_on_login_page, email)

    def enter_password_input_field_on_login_page(self, password):
        self.input_element(self.password_input_field_on_login_page, password)

    def verify_login_using_other_accounts_label(self):
        self.verify_element_display(self.login_using_other_accounts_label)
        
    def verify_please_provide_a_valid_email_msg(self):
        self.verify_element_display(self.please_provide_a_valid_email_msg)

    def verify_please_provide_password_msg(self):
        self.verify_element_display(self.please_provide_password_msg)

    def verify_unable_to_login_with_provided_credentials(self):
        self.verify_element_display(self.unable_to_login_with_provided_credentials)
