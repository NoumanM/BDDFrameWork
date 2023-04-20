from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
import DashboardPageSteps


@then(u'Click on Profile Icon')
def click_on_profile_icon(context):
    try:
        DashboardPageSteps.click_profile_icon_on_dashboard_page(context)
        DashboardPageSteps.verify_information_labels_on_profile_page(context)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on profile icon"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Upload a profile picture')
def upload_a_profile_icon(context):
    try:
        context.ProfilePage.change_profile_pic()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Uploading a profile picture"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e



@then(u'Verify all fields on profile page are displaying')
def verify_all_fields_on_profile_page_are_displaying(context):
    try:
        context.ProfilePage.verify_first_name_input_field()
        context.ProfilePage.verify_last_name_input_field()
        context.ProfilePage.verify_email_input_field()
        context.ProfilePage.verify_phone_input_field()
        context.ProfilePage.verify_reset_my_password()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verifying all fields on profile page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Enter first name and last name on profile page')
def verify_all_fields_on_profile_page_are_displaying(context):
    try:
        context.ProfilePage.enter_first_name()
        context.ProfilePage.enter_last_name()
        context.ProfilePage.enter_phone_number()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Entering first name and last name"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify saved successfully message is displaying')
def verify_all_fields_on_profile_page_are_displaying(context):
    try:
        context.ProfilePage.verify_saved_successfully_msg()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Saved changes message is not displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click save changes btn')
def click_saveChanges_btn(context):
    try:
        context.ProfilePage.click_saveChanges_btn()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on click save changes button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify correct email is displaying')
def verify_email_input_field_contains_correct_email(context):
    try:
        context.ProfilePage.verify_email_input_field_contains_correct_email()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify correct email is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Enter a phone number')
def enter_phone_number(context):
    try:
        context.ProfilePage.enter_phone_number()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Entering a phone number"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Enter a invalid phone number')
def enter_invalid_phone_number(context):
    try:
        context.ProfilePage.enter_invalid_phone_number()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Entering an invalid phone number"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify a invalid phone number message')
def verify_invalid_phone_number_msg(context):
    try:
        context.ProfilePage.verify_invalid_phone_number_msg()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify a invalid phone number message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify a invalid email address message')
def verify_invalid_email_address_msg(context):
    try:
        context.ProfilePage.verify_invalid_email_address_msg()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify a invalid email address message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Enter a invalid email address')
def enter_email_input_field(context):
    try:
        context.ProfilePage.enter_email_input_field()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Enter a invalid email address"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Verify day, month and date on left side of profile page')
def verify_today_and_todate(context):
    try:
        context.ProfilePage.verify_today_and_todate()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify day, month and date on left side of profile page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Upload profile picture')
def step_impl(context):
    try:
        context.ProfilePage.upload_profile_picture()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Upload profile picture"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e