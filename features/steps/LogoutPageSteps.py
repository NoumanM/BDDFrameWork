from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from pages.LogoutPage import LogoutPage



@then(u'Click on logout button')
def click_logout_btn(context):
    try:
        context.LogoutPage.click_logout_btn()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on logout button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e