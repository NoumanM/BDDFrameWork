import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        self.wait(1)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        self.wait(2)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'})", element)
        self.wait(2)
        element.click()

    def click_using_js(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)

    def input_element(self, by_locator, text):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL, '\A', '\b')
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_display(self, by_locator):
        self.wait(2)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).is_displayed()

    def verify_element_not_display(self, by_locator):
        self.wait(2)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).is_displayed()
            if not element:
                return True
        except:
            return False

    def verify_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return element.is_enabled()

    def get_web_element(self, by_locator):
       element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
       return element

    def get_web_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def wait(self, seconds=3):
        time.sleep(seconds)

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def assert_equal(self,actual_value, expected_value, Message):
        assert actual_value == expected_value,Message

    def verify_element_disabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return not (element.is_enabled())

    def generate_random_email(self, value):
        digits = random.randint(1000, 9999)
        return str(value) + str(digits) + '@codeautomation.ai'

    def generate_random_password(self, value):
        digits = random.randint(1000,9999)
        return str(value) + str(digits)

    def generate_random_data_against_a_keyword(self, value):
        digits = random.randint(1000, 9999)
        return str(value) + str(digits)

    def get_attribute_of_a_element(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)


    def generate_random_phone_number(self):
        digits = random.randint(1000000, 9999999)
        return '1613' + str(digits)