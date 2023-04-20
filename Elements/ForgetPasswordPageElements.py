from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ForgetPasswordPageElements(BasePage):
    i_forget_my_password_link = (By.XPATH, "//a[contains(text(),'I forgot my password')]")
    forget_password_label = (By.XPATH, "//div[contains(text(),'Forgot Password')]")
    reset_my_password_button = (By.XPATH, "//button[contains(text(),'Reset my password')]")
    an_email_has_been_sent_msg = (By.XPATH, "//div[contains(text(),'An email has been sent to provided email address.')]")


