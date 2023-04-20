from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProfilePageElements(BasePage):
    profile_img_input = (By.XPATH, "//input[contains(@name,'avatar[image]')]")
    first_name_input_field = (By.XPATH, "//input[contains(@name,'first_name')]")
    last_name_input_field = (By.XPATH, "//input[contains(@name,'last_name')]")
    email_input_field = (By.XPATH, "//input[contains(@name,'email')]")
    phone_input_field = (By.XPATH, "//input[contains(@type,'tel')]")
    reset_my_password = (By.XPATH, "//a[contains(text(),'Reset my password')]")
    saveChanges_btn = (By.XPATH, "//button[contains(text(),'Save Changes')]")
    saved_successfully = (By.XPATH, "//div[contains(text(),'Saved successfully')]")
    invalid_phone_number_msg = (By.XPATH, "//div[contains(text(),'Must be a valid phone number')]")
    invalid_email_address_msg = (By.XPATH, "//div[contains(text(),'Email must be a valid email')]")

