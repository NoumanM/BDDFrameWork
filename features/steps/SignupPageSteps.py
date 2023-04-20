from behave import *
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from pages.BasePage import BasePage

@then(u'Verify Habit Accountability Tracking logo is displaying')
def habit_accountability_logo(context):
    try:
        context.SignupPage.verify_hat_logo()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(e+"Test Failed to Verify Habit Accountability Logo"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify Habit Accountability Logo"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify Habit Accountability Logo"

@then(u'Verify Sign up button is displaying')
def verify_signup_button_is_displaying(context):
    try:
        context.SignupPage.verify_signup_button_is_displaying()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed to Verify Sign up is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify Sign up is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify Sign up is displaying"

@then(u'Click Sign up button')
def click_signup_button(context):
    try:
        context.SignupPage.click_on_signup_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(e+"Test Failed to Click Sign up button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Click Sign up button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Click Sign up button"


@when(u'Enter email address on signup page')
def enter_email_address(context):
    try:
        context.SignupPage.enter_email_address_on_signup_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) +"Test Failed to Enter email address on signup page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter email address on signup page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter email address on signup page"

@when(u'Enter password and confirm password')
def enter_password_and(context):
    try:
        password = BasePage.generate_random_password(context, 'Test#')
        context.SignupPage.enter_password_on_signup_page(password)
        context.SignupPage.enter_confirm_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter password and confirm passsword"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter password and confirm passsword"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter password and confirm passsword"

@when(u'Enter password')
def enter_password_on_signup_page(context):
    try:
        password = BasePage.generate_random_password(context, 'Test#')
        context.SignupPage.enter_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter password "),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter password"

@when(u'Enter confirm password')
def click_signup_button(context):
    try:
        password = BasePage.generate_random_password(context, 'Test#')
        context.SignupPage.enter_confirm_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter confirm passsword"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter confirm passsword"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter confirm passsword"

@when(u'Check i agree checkbox')
def check_i_agree_check_box(context):
    try:
        context.SignupPage.click_i_agree_checkbox()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Check i agree checkbox"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Check i agree checkbox"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Check i agree checkbox"

@then(u'Verify this field may not be empty message')
def verify_this_field_may_not_be_empty_msg(context):
    try:
        context.SignupPage.verify_this_field_may_not_be_empty_msg()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Verify this field may not be empty message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify this field may not be empty message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify this field may not be empty message"

@then(u'Verify password should be same as confirm password message')
def verify_password_should_be_same_as_confirm_password_msg(context):
    try:
        context.SignupPage.verify_password_should_be_same_as_confirm_password()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed to Verify password should be same as confirm password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed to Verify password should be same as confirm password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify password should be same as confirm password message"

@then(u'Verify You must accept our terms of agreement before completing sign up message')
def verify_you_must_accept_our_terms(context):
    try:
        context.SignupPage.verify_you_must_accept_our_terms()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed to Verify You must accept our terms of agreement before completing sign up message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed to You must accept our terms of agreement before completing sign up message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to You must accept our terms of agreement before completing sign up message"

@then(u'Verify enter a valid email message')
def verify_enter_a_valid_email_msg(context):
    try:
        context.SignupPage.verify_enter_a_valid_email_msg()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed to Verify enter a valid email message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed to Verify enter a valid email message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify enter a valid email message"

@then(u'Enter an invalid email address')
def enter_invalid_email_address_on_signup_page(context):
    try:
        context.SignupPage.enter_invalid_email_address_on_signup_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed to Enter an invalid email address"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed to Enter an invalid email address"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter an invalid email address"

@when(u'Enter invalid password and confirm password')
def enter_invalid_password(context):
    try:
        password = BasePage.generate_random_password(context, 'Test')
        context.SignupPage.enter_password_on_signup_page(password)
        context.SignupPage.enter_confirm_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter invalid password and confirm password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter invalid password and confirm password"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter invalid password and confirm password"


@then(u'Verify invalid password message')
def verify_enter_minimum_eight_character_password_msg(context):
    try:
        password = BasePage.generate_random_password(context, 'Test')
        context.SignupPage.enter_password_on_signup_page(password)
        context.SignupPage.enter_confirm_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Verify invalid password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify invalid password message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify invalid password message"

@then(u'Verify password length should be minimum 8 characters message')
def verify_password_length_should_be_minimum_8_characters(context):
    try:
        context.SignupPage.verify_password_length_should_be_minimum_8_characters()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed to Verify passsword length should be minimum 8 characters message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed to Verify passsword length should be minimum 8 characters message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify passsword length should be minimum 8 characters message"

@then(u'Enter password less than 8 characters')
def enter_minimum_eight_character_password_msg(context):
    try:
        password = BasePage.generate_random_password(context, 'T#')
        context.SignupPage.enter_password_on_signup_page(password)
        context.SignupPage.enter_confirm_password_on_signup_page(password)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter password less than 8 characters"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter password less than 8 characters"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter password less than 8 characters"

@then(u'Verify register a new account label')
def verify_register_new_account_label(context):
    try:
        context.SignupPage.verify_register_new_account_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Verify register a new account label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify register a new account label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify register a new account label"


@then(u'Verify google icon and signup with other accounts is displaying')
def verify_google_icon_and_signup_with_other_account(context):
    try:
        context.SignupPage.verify_signup_using_other_accounts()
        context.SignupPage.verify_google_icon_on_signup_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Verify google icon and signup with other accounts is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Verify google icon and signup with other accounts is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Verify google icon and signup with other accounts is displaying"


@then(u'Enter unregister email address')
def enter_unregister_email_address(context):
    try:
        context.SignupPage.enter_unregister_email_address()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e)+"Test Failed to Enter unregister email address"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed to Enter unregister email address"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed to Enter unregister email address"