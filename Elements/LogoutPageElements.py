from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LogoutPageElements(BasePage):
    logout_btn = (By.XPATH, "//button[contains(text(),'Logout')]")