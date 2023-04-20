from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
import random
import string
# from numpy.distutils.command.config import config
from pages.BasePage import BasePage
from Constants.config import TestData

@then(u'Verify i forget my password link')
def verify_i_forget_my_password_link(context):
    try:
        context.ForgetPasswordPage.verify_i_forget_my_password_link()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify i forget my password link"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify i forget my password link"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify i forget my password link"


@then(u'Click on i forget my password link')
def click_on_i_forget_my_password_link(context):
    try:
        context.ForgetPasswordPage.click_on_i_forget_my_password_link()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Click on i forget my password link"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click on i forget my password link"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on i forget my password link"


@then(u'Verify forget password label')
def verify_forget_password_label(context):
    try:
        context.ForgetPasswordPage.verify_forget_password_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Verify forget password label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify forget password label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify forget password label"



@then(u'Click on reset password button')
def click_on_reset_my_password_button(context):
    try:
        context.ForgetPasswordPage.click_on_reset_my_password_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on Click on reset password button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click on reset password button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on reset password button"

@then(u'Verify An email has been sent to provided email address message')
def verify_an_email_has_been_sent_msg(context):
    try:
        context.ForgetPasswordPage.verify_an_email_has_been_sent_msg()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed on An email has been sent to provided email address message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on An email has been sent to provided email address message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on An email has been sent to provided email address message"