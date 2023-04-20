from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
import random
import string
# from numpy.distutils.command.config import config
from pages.BasePage import BasePage
from Constants.config import TestData
import DashboardPageSteps
from pages.DashboardPage import DashboardPage
import SignupPageSteps
import loginsteps

option = ''
sub_category_name = ''

@then(u'Click on category button under Add new button')
def click_on_category_button_under_add_new_button(context):
    try:
        SignupPageSteps.habit_accountability_logo(context)
        DashboardPageSteps.click_add_new_button_and_verify_dropdown_options(context)
        DashboardPageSteps.click_category_button_and_verify_popup_window(context)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on category button under Add new button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Select option against area against area')
def select_area_on_add_new_category_popup_window(context):
    try:
        context.AddNewCategoryPage.select_area_on_add_new_category_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Select option against area against area"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'"{value}" category on add new category popup window')
def select_category_on_add_new_category_popup_window(context, value):
    try:
        global option
        option = context.AddNewCategoryPage.select_category_on_add_new_category_popup_window(value)
        if type(option) == 'str':
            attach(option,
                   "Selected option",
                   attachment_type=AttachmentType.TEXT)
        if type(option) == 'list':
            for i in option:
                attach(i,
                       "options ",
                       attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Select category on add new category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
@then(u'Add button on add new category popup window "{val}"')
def click_add_btn_on_add_a_new_note_popup_window(context, val):
    try:
        context.AddNewCategoryPage.click_add_button(val)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click add button on add new category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify added category and add new category popup window')
def verify_add_new_category_popup_window_and_added_category(context):
    try:
        context.AddNewCategoryPage.verify_added_category_under_daily_progress(option)

        if DashboardPage.verify_add_new_category_popup_window(context):
            return False
        else:
            return True
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click add button on add new category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click dropdown icon against area')
def click_dropdown_against_area(context):
    try:
        context.AddNewCategoryPage.click_dropdown_against_area()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click dropdoown icon against area"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'select category dropdown "{value}"')
def verify_select_category_dropdown(context, value):
    try:
        context.AddNewCategoryPage.verify_select_category_is_disabled(value)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify select category dropdown is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'verify "{val}" list of options displaying')
def verify_select_category_dropdown_is_disabled(context,val):
    try:
        select_category_on_add_new_category_popup_window(context, val)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify select category dropdown is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'verify category weight dropdown "{val}"')
def verify_category_weight_dropdown(context, val):
    try:
        context.AddNewCategoryPage.verify_category_weight_dropdown(val)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on verify category weight dropdown"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'verify category weight value')
def get_category_weight_value(context):
    try:
        context.AddNewCategoryPage.get_category_weight_value()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on verify category weight value"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click on sub category button under Add new button')
def click_on_subcategory_button_under_add_new_button(context):
    try:
        SignupPageSteps.habit_accountability_logo(context)
        DashboardPageSteps.click_add_new_button_and_verify_dropdown_options(context)
        DashboardPageSteps.click_subcategory_button_and_verify_popup_window(context)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on category button under Add new button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Sub category name field "{func}"')
def click_on_subcategory_button_under_add_new_button(context, func):
    try:
        if func == 'enter':
            global sub_category_name
            name = BasePage.generate_random_data_against_a_keyword(context, 'sub category')
            context.AddNewCategoryPage.sub_category_name_field_functions(func, name)

        else:
            context.AddNewCategoryPage.sub_category_name_field(func, '')
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on category button under Add new button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e



@then(u'Verify sub category on dashboard')
def verify_sub_Category(context):
    try:
        global sub_category_name
        context.AddNewCategoryPage.verify_sub_Category(sub_category_name)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on category button under Add new button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e