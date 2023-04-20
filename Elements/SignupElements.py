from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SignupElements(BasePage):
    hat_logo = (By.XPATH, "//div[contains(text(),'Habit Accountability Tracker')]")
    signup_button = (By.XPATH, "//button[contains(text(),'sign up')]")
    email_field = (By.XPATH, "//input[contains(@name,'email')]")
    password_field =(By.XPATH, "//input[contains(@name,'password')]")
    confirm_password_field = (By.XPATH, "//input[contains(@name,'confirmPassword')]")
    agree_check_box = (By.XPATH, "//input[contains(@name,'agree')]")
    this_field_may_not_be_empty_msg = (By.XPATH, "//div[contains(text(),'This field may not be blank.')]")
    password_should_be_same_as_confirm_password = (By.XPATH, "//small[contains(text(),'Confirm password should be same as password.')]")
    you_must_accept_our_terms = (By.XPATH, "//span[contains(text(),'You must accept our terms of agreement before completing sign up.')]")
    enter_a_valid_email_msg = (By.XPATH, "//div[contains(text(),'Enter a valid email address.')]")
    enter_minimum_eight_character_password = (By.XPATH, "//small[contains(text(),'Please enter minimum 8 characters password')]")
    password_length_should_be_minimum_8_characters = (By.XPATH, "//small[contains(text(),'Password length should be minimum 8 character.')]")
    register_new_account_label = (By.XPATH, "//div[contains(text(),'Register new account')]")
    signup_using_other_accounts = (By.XPATH, "//div[contains(text(),'Sign up using other accounts')]")
    google_icon_on_signup_page = (By.XPATH,"//img[@alt='google']")







