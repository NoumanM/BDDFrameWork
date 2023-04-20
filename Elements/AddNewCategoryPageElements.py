from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AddNewCategoryPageElements(BasePage):
    dropdown_icon_against_area = (By.XPATH, "//label[contains(text(),'Area ')]/following-sibling::div/div/div/div/div")
    dropable_options_on_add_new_category = (By.XPATH, "//div[contains(@class,'css-9g7j0m-menu')]/div/div")
    select_category = (By.XPATH, "//div[contains(text(),'Select or create your own category')] | //div[contains(text(),'Select category')]")
    add_btn_on_add_a_new_note = (By.XPATH, "//button[text()='Add']")
    category_weight_dropdown = (By.XPATH, "(//div[contains(@class,'col-8')])[3]")
    category_weight_value = (By.XPATH, "(//div[contains(@class,' css-1dhrhzn-singleValue')])")
    sub_category_name_field = (By.XPATH, "//input[contains(@placeholder,'Enter name of subcategory')]")

