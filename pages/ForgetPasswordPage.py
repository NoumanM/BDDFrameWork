import datetime
import os
import mysql.connector
from selenium.webdriver.support.select import Select
from Elements.LoginPageElements import LoginPageElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.config import TestData
from pages.SignupPage import SignupPage
from Elements.ForgetPasswordPageElements import ForgetPasswordPageElements



class ForgetPasswordPage(ForgetPasswordPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_i_forget_my_password_link(self):
        self.verify_element_display(self.i_forget_my_password_link)

    def click_on_i_forget_my_password_link(self):
        self.click_element(self.i_forget_my_password_link)

    def verify_forget_password_label(self):
        self.verify_element_display(self.forget_password_label)

    def click_on_reset_my_password_button(self):
        self.click_element(self.reset_my_password_button)

    def verify_an_email_has_been_sent_msg(self):
        self.verify_element_display(self.an_email_has_been_sent_msg)