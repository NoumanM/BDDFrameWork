from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPageElements(BasePage):
    login_label = (By.XPATH, "(//div[contains(text(),'Login')])[1]")
    login_button = (By.XPATH, "//button[contains(text(),'login')]")
    email_input_field_on_login_page = (By.XPATH, "//input[contains(@name,'email')]")
    password_input_field_on_login_page = (By.XPATH, "//input[contains(@name,'password')]")
    login_using_other_accounts_label =(By.XPATH, "//div[contains(text(),'Login using other accounts')]")
    please_provide_a_valid_email_msg = (By.XPATH, "//div[contains(text(),'Please provide valid email.')]")
    please_provide_password_msg = (By.XPATH, "//div[contains(text(),'Please provide password.')]")
    unable_to_login_with_provided_credentials = (By.XPATH, "//div[contains(text(),'Unable to log in with provided credentials.')]")



