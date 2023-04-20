from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
import random
import string
# from numpy.distutils.command.config import config
from pages.BasePage import BasePage
from Constants.config import TestData


@then(u'Verify login label is displayed')
def verify_login_label_is_dispaying(context):
    try:
        context.loginPage.verify_login_label_is_displayed()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify login label is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify login label is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify login label is displayed"


@then(u'Verify login button on signup page')
def verify_login_button_on_signup_page(context):
    try:
        context.loginPage.verify_login_button_on_signup_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify login button on signup page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify login button on signup page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify login button on signup page"

@then(u'Click login button')
def click_login_button(context):
    try:
        context.loginPage.click_login_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click login button"

@then(u'Login with valid email and password')
def click_login_button(context):
    try:
        context.loginPage.enter_email_input_field_on_login_page(TestData.email)

        context.loginPage.enter_password_input_field_on_login_page(TestData.password)
        context.loginPage.click_login_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Login with valid email and password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Login with valid email and password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Login with valid email and password"


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()

@then(u'Verify user successfully logout')
@then(u'Verify google icon and sigin with other accounts label')
def verify_google_icon_and_sigin_with_other_accounts_label(context):
    try:
        context.loginPage.verify_login_using_other_accounts_label()
        context.SignupPage.verify_google_icon_on_signup_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify google icon and sigin with other accounts label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify google icon and sigin with other accounts label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify google icon and sigin with other accounts label"


@then(u'Enter password and click login button')
def enter_password_on_login_screen_and_click_login_button(context):
    try:
        password = TestData.password
        context.loginPage.enter_password_input_field_on_login_page(password)
        context.loginPage.click_login_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Enter password and click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Enter password and click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Enter password and click login button"


@then(u'Verify please provide a valid email message')
def enter_password_on_login_screen_and_click_login_button(context):
    try:
        context.loginPage.verify_please_provide_a_valid_email_msg()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify please provide a valid email message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify please provide a valid email message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify please provide a valid email message"


@then(u'Enter valid email and click login button')
def click_login_button(context):
    try:
        context.loginPage.enter_email_input_field_on_login_page()
        context.loginPage.click_login_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Enter valid email and click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Enter valid email and click login button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Enter valid email and click login button"

@then(u'Verify please provide password message')
def verify_please_provide_password_msg(context):
    try:
        context.loginPage.verify_please_provide_password_msg()
        context.loginPage.click_login_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify please provide password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify please provide password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify please provide password message"

@then(u'Verify unable to login with provided credentials message')
def verify_unable_to_login_with_provided_credentials_msg(context):
    try:
        context.loginPage.verify_unable_to_login_with_provided_credentials()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify unable to login with provided credentials message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify unable to login with provided credentials message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify unable to login with provided credentials message"


@then(u'Enter valid login email "{email}"')
def enter_valid_login_email(context, email):
    try:
        context.loginPage.enter_email_input_field_on_login_page(email)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Enter valid login email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Enter valid login email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Enter valid login email"

@then(u'Enter invalid login password "{passw}"')
def click_login_button(context, passw):
    try:
        password = BasePage.generate_random_password(context, passw)
        context.loginPage.enter_password_input_field_on_login_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Enter valid login email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Enter valid login email"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Enter valid login email"