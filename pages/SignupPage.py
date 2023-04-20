import random
import string
from datetime import datetime
import os
from selenium.webdriver.support.select import Select
from Elements.SignupElements import SignupElements
from Elements.LoginPageElements import LoginPageElements


class SignupPage(SignupElements, LoginPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_hat_logo(self):
        self.wait(1)
        self.verify_element_display(self.hat_logo)

    def verify_signup_button_is_displaying(self):
        self.wait(1)
        self.verify_element_display(self.signup_button)

    def click_on_signup_button(self):
        self.wait(1)
        self.click_element(self.signup_button)

    def enter_email_address_on_signup_page(self):
        self.wait(2)
        self.input_element(self.email_field, self.generate_random_email('Test'))

    def enter_password_on_signup_page(self, password):
        self.wait(1)
        self.input_element(self.password_field, password)

    def enter_confirm_password_on_signup_page(self, password):
        self.wait(1)
        self.input_element(self.confirm_password_field, password)

    def click_i_agree_checkbox(self):
        self.wait(1)
        self.click_element(self.agree_check_box)

    def verify_login_label_is_displaying(self):
        self.wait(1)
        self.verify_element_display(self.login_label)

    def verify_this_field_may_not_be_empty_msg(self):
        self.verify_element_display(self.this_field_may_not_be_empty_msg)

    def verify_password_should_be_same_as_confirm_password(self):
        self.verify_element_display(self.password_should_be_same_as_confirm_password)

    def verify_you_must_accept_our_terms(self):
        self.verify_element_display(self.you_must_accept_our_terms)

    def verify_enter_a_valid_email_msg(self):
        self.verify_element_display(self.enter_a_valid_email_msg)

    def enter_invalid_email_address_on_signup_page(self):
        self.wait(1)
        self.input_element(self.email_field, self.generate_random_email('@'))

    def verify_enter_minimum_eight_character_password(self):
        self.verify_element_display(self.enter_minimum_eight_character_password)

    def verify_password_length_should_be_minimum_8_characters(self):
        self.verify_element_display(self.password_length_should_be_minimum_8_characters)

    def verify_register_new_account_label(self):
        self.verify_element_display(self.register_new_account_label)

    def verify_signup_using_other_accounts(self):
        self.verify_element_display(self.signup_using_other_accounts)

    def verify_google_icon_on_signup_page(self):
        self.verify_element_display(self.google_icon_on_signup_page)

    def enter_unregister_email_address(self):
        self.input_element(self.email_field, self.generate_random_email('unregisterTest'))


