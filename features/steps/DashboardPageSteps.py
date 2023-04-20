from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
import random
import string
# from numpy.distutils.command.config import config
from pages.BasePage import BasePage
from Constants.config import TestData


note = ''
@then(u'Verify progress bar')
def verify_progress_bar(context):
    try:
        context.DashboardPage.verify_progress_bar()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify progress bar is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify progress bar is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify progress bar is displayed"


@then(u'Verify weekly points')
def verify_weekly_points(context):
    try:
        context.DashboardPage.verify_weekly_points()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify weekly points is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify weekly points is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify weekly points is displayed"


@then(u'Verify tracking week')
def verify_tracking_week(context):
    try:
        context.DashboardPage.verify_tracking_week()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify tracking week is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify tracking week is displayed"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify tracking week is displayed"


@then(u'Click on tracking week date picker')
def click_on_tracking_week(context):
    try:
        context.DashboardPage.click_on_tracking_week()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on tracking week date picker"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click on tracking week date picker"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on tracking week date picker"


@then(u'Verify tracking week day picker')
def verify_tracking_week_day_picker(context):
    try:
        context.DashboardPage.verify_tracking_week_day_picker()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify tracking week day picker display"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify tracking week day picker display"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify tracking week day picker display"


@then(u'Verify week score, week days avg, weekend avg progress bar')
def verify_weekScore_weekDaysAvg_weekEndAvg_progress_bar(context):
    try:
        context.DashboardPage.verify_weekScore_weekDaysAvg_weekEndAvg_progress_bar()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(
            str(e) + "Test Failed on Verify week score, week days avg, weekend avg progress bar is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify week score, week days avg, weekend avg progress bar is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify week score, week days avg, weekend avg progress bar is displaying"


@then(u'Verify modify view with icon')
def verify_modify_view_with_eye_icon(context):
    try:
        context.DashboardPage.verify_modify_view_with_eye_icon()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify modify view with icon is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify modify view with icon is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify modify view with icon is displaying"


@then(u'Verify daily score all area label and chart')
def verify_daily_score_all_areas_chart(context):
    try:
        context.DashboardPage.verify_daily_score_all_areas_chart()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify daily score all area label and chart is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify daily score all area label and chart is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify daily score all area label and chart is displaying"


@then(u'Verify daily score all area dropdown')
def verify_daily_score_all_area_dropdown(context):
    try:
        context.DashboardPage.verify_daily_score_all_area_dropdown()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify daily score all area dropdown is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify daily score all area dropdown is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify daily score all area dropdown is displaying"


@then(u'Click on daily score all area dropdown')
def click_on_daily_score_all_area_dropdown(context):
    try:
        context.DashboardPage.click_on_daily_score_all_area_dropdown()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on daily score all area dropdown"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on daily score all area dropdown"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on daily score all area dropdown"


@then(u'Verify daily score all area dropdown options')
def verify_daily_score_all_area_dropdown_options(context):
    try:
        options = context.DashboardPage.verify_daily_score_all_area_dropdown_options()
        for opt in options:
            attach(opt,
                   "available options",
                   attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify daily score all area dropdown  optionsis displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify daily score all area dropdown options is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify daily score all area dropdown options is displaying"


@then(u'Verify activity journal')
def verify_activity_journal(context):
    try:

        context.DashboardPage.verify_activity_journal()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify activity journal is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Verify activity journal is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify activity journal is displaying"


@then(u'Verify quote of the section')
def verify_quote_of_the_day(context):
    try:

        context.DashboardPage.verify_quote_of_the_day()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify quote of the section is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify quote of the section is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify quote of the section is displaying"


@then(u'Verify add new button under tracking week')
def verify_add_new_button_under_tracking_week(context):
    try:

        context.DashboardPage.verify_add_new_button_under_tracking_week()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify add new button under tracking week is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify add new button under tracking week is displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify add new button under tracking week is displaying"


@then(u'Click on modify view with eye icon')
def click_on_modify_view_with_eye_icon(context):
    try:

        context.DashboardPage.click_on_modify_view_with_eye_icon()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on modify view with eye icon"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click on modify view with eye icon"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on modify view with eye icon"


@then(u'Verify display data label and daily progress label')
def verify_display_data_label_and_daily_progress_label(context):
    try:

        context.DashboardPage.verify_display_data_label_and_daily_progress_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify display data label and daily progress label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify display data label and daily progress label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify display data label and daily progress label"


@then(u'Verify field against display data and daily progress label')
def verify_field_against_display_data_button_and_field_against_daily_progress_button(context):
    try:

        context.DashboardPage.verify_field_against_display_data_button_and_field_against_daily_progress_button()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify field against display data and daily progress label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify field against display data and daily progress label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify field against display data and daily progress label"


@then(u'Verify collapse all and expand all buttons on modify view popup')
def verify_collapse_all_button_and_expand_all_button_on_modify_view(context):
    try:

        context.DashboardPage.verify_collapse_all_button_and_expand_all_button_on_modify_view()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify collapse all and expand all buttons on modeify view popup"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify collapse all and expand all buttons on modeify view popup"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify collapse all and expand all buttons on modeify view popup"


@then(u'Click add new button and verify dropdown options')
def click_add_new_button_and_verify_dropdown_options(context):
    try:
        context.DashboardPage.click_on_add_new_button_under_tracking_week()
        options = context.DashboardPage.verify_add_new_button_dropdown_options()
        for opt in options:
            attach(opt,
                   "available options",
                   attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify add new dropdown options are displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify add new dropdown options are displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify add new dropdown options are displaying"


@then(u'Verify display data dropdown options')
def verify_add_new_button_dropdown_options(context):
    try:
        context.DashboardPage.click_on_field_against_display_data_label()
        options = context.DashboardPage.verify_options_against_display_data_label()
        for opt in options:
            attach(opt,
                   "available options",
                   attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on display data dropdown options are displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on display data dropdown options are displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on display data dropdown options are displaying"


@then(u'Click on radio button against daily progress')
def click_on_radio_btn_against_daily_progress(context):
    try:
        context.DashboardPage.click_on_radio_btn_against_daily_progress()
        context.DashboardPage.click_on_radio_btn_against_daily_progress()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on radio button against daily progress"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on radio button against daily progress"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on radio button against daily progress"


@then(u'Verify daily progress label on dashboard')
def verify_daily_progress_label_on_dashboard(context):
    try:
        if not context.DashboardPage.verify_daily_progress_label_on_dashboard():
            return True
        else:
            return True
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify daily progress label on dashboard"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify daily progress label on dashboard"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify daily progress label on dashboard"


@then(u'Click on collapse all button on modify view')
def verify_daily_progress_label_on_dashboard(context):
    try:
        context.DashboardPage.click_on_collapse_all_button_on_modify_view()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on collapse all button on modify view"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on collapse all button on modify view"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on collapse all button on modify view"


@then(u'Verify collapse all button is disabled')
def verify_collapse_all_button_on_modify_view_is_disabled(context):
    try:
        context.DashboardPage.verify_collapse_all_button_on_modify_view_is_disabled()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify collapse all button is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify collapse all button is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify collapse all button is disabled"


@then(u'Verify sub dropables under health "{option}"')
def verify_nutrition_flexibility_headache_weight_subdropables_under_health_is_not_displaying(context, option):
    try:
        if option == 'Collapse All':
            context.DashboardPage.verify_nutrition_flexibility_headache_weight_subdropables_under_health_is_not_displaying()
        else:
            if not context.DashboardPage.verify_nutrition_flexibility_headache_weight_subdropables_under_health_is_not_displaying():
                return True
            else:
                return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify sub dropables under health not displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify sub dropables under health not displaying"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify sub dropables under health not displaying"


@then(u'Click on expand all button on modify view')
def click_on_expand_all_button_on_modify_view(context):
    try:
        context.DashboardPage.click_on_expand_all_button_on_modify_view()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on expand all button on modify view"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on expand all button on modify view"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on expand all button on modify view"


@then(u'Click on expand all button on modify view is disabled')
def verify_expand_all_button_on_modify_view_is_disabled(context):
    try:
        context.DashboardPage.verify_expand_all_button_on_modify_view_is_disabled()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on expand all button on modify view is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on expand all button on modify view is disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on expand all button on modify view is disabled"


@then(u'Click on category button and verify add new category popup window')
def click_category_button_and_verify_popup_window(context):
    try:
        context.DashboardPage.click_on_category_btn()
        context.DashboardPage.verify_add_new_category_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on category button and verify add new category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on category button and verify add new category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on category button and verify add new category popup window"


@then(u'Click on sub category button and verify add new sub category popup window')
def click_subcategory_button_and_verify_popup_window(context):
    try:
        context.DashboardPage.click_on_subCategory_btn()
        context.DashboardPage.verify_add_new_subCategory_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(
            str(e) + "Test Failed on Click on sub category button and verify add new sub category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on sub category button and verify add new sub category popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on sub category button and verify add new sub category popup window"


@then(u'Click on habit button and verify add new habit popup window')
def click_habit_button_and_verify_popup_window(context):
    try:
        context.DashboardPage.click_on_habit_btn()
        context.DashboardPage.verify_add_new_habit_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click on habit button and verify add new habit popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click on habit button and verify add new habit popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click on habit button and verify add new habit popup window"


@then(u'Click x icon on popup window')
def click_on_x_icon_on_popup_window(context):
    try:
        context.DashboardPage.click_on_x_icon_on_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(), name=str(str(e) + "Test Failed on Click x icon on popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click x icon on popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click x icon on popup window"


@then(u'Click cancel button on popup window')
def click_on_cancel_btn_on_popup_window(context):
    try:
        context.DashboardPage.click_on_cancel_btn_on_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click cancel button on popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Click cancel button on popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click cancel button on popup window"


@then(u'Verify the popup window "{window}"')
def verify_the_popup_window(context, window):
    try:
        if window == 'category':
            if not context.DashboardPage.verify_add_new_category_popup_window():
                return True
            else:
                return False
        if window == 'sub category':
            if not context.DashboardPage.verify_add_new_subCategory_popup_window():
                return True
            else:
                return False
        else:
            if not context.DashboardPage.verify_add_new_habit_popup_window():
                return True
            else:
                return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + f"Test Failed on Verify the popup window {window}"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str(f"Test Failed on Verify the popup window {window}"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, f"Test Failed on Verify the popup window {window}"


@then(u'Click plus button against todate in activity journal')
def click_plus_button_against_todate_in_activity_journal(context):
    try:
        context.DashboardPage.click_plus_button_against_todate_in_activity_journal()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click plus button against todate in activity journal"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click plus button against todate in activity journal"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click plus button against todate in activity journal"


@then(u'Verify add new note popup window "{check}"')
def verify_add_new_note_popup_window(context, check):
    try:
        if check == 'displaying':
            context.DashboardPage.verify_add_new_note_popup_window()
        else:
            if not context.DashboardPage.verify_add_new_note_popup_window():
                return True
            else:
                return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify add new note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify add new note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify add new note popup window"


@then(u'Click profile icon on dashboard page')
def click_profile_icon_on_dashboard_page(context):
    try:
        context.DashboardPage.click_profile_icon_on_dashboard_page()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click profile icon on dashboard page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click profile icon on dashboard page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click profile icon on dashboard page"


@then(u'Verify information labels on profile page')
def verify_information_labels_on_profile_page(context):
    try:
        context.DashboardPage.verify_personal_information_label()
        context.DashboardPage.verify_contact_information_label()
        context.DashboardPage.verify_login_information_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify information labels on profile page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify information labels on profile page"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify information labels on profile page"


@then(u'Verify day capital letters on activity journal')
def verify_day_capital_letters_on_activity_journal(context):
    try:
        options = context.DashboardPage.verify_day_capital_letters_on_activity_journal()
        for opt in options:
            attach(opt,
                   "Day Capital Letters: ",
                   attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify day capital letters on activity journal"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify day capital letters on activity journal"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify day capital letters on activity journal"


@then(u'Choose location from location input field on add note popup window add note and click on add button')
def verify_select_location_from_location_input_field_on_add_note_popup_window_add_note_and_click_on_add_button(context):
    try:
        global note
        note = context.BasePage.generate_random_data_against_a_keyword('Note')
        context.DashboardPage.select_location_from_location_input_field_on_add_note_popup_window()
        context.DashboardPage.add_note_on_add_a_new_note_popup_window(note)
        context.DashboardPage.click_add_btn_on_add_a_new_note_popup_window()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify select location from location input field on add note popup window add note and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Verify select location from location input field on add note popup window add note and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify select location from location input field on add note popup window add note and click on add button"


@then(u'Verify three dots button on new note "{val}"')
def verify_three_dots_btn_on_new_note_activity_journal(context, val):
    try:
        if val == 'click':
            context.DashboardPage.verify_three_dots_btn_on_new_note_activity_journal(note, val)
        else:
            if val == 'displaying':
                context.DashboardPage.verify_three_dots_btn_on_new_note_activity_journal(note, val)
            else:
                val = ''
                if not context.DashboardPage.verify_three_dots_btn_on_new_note_activity_journal(note, val):
                    return True
                else:
                    return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify three dots button on new note"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Verify three dots button on new note"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify three dots button on new note"

@then(u'Verify edit note link under three dots button "{val}"')
def verify_edit_note_link_under_three_dots_btn(context, val):
    try:
        if val == 'click':
            context.DashboardPage.verify_edit_note_link_under_three_dots_btn(val)
        else:
            val = ''
            context.DashboardPage.verify_edit_note_link_under_three_dots_btn(val)

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify edit note link under three dots button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify edit note link under three dots button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify edit note link under three dots button"


@then(u'Verify delete note link under three dots button "{value}"')
def verify_delete_note_link_under_three_dots_btn(context, value):
    try:

       if value == 'click':
           context.DashboardPage.verify_delete_note_link_under_three_dots_btn(value)

       else:
           value = ''
           context.DashboardPage.verify_delete_note_link_under_three_dots_btn(value)

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Verify delete note link under three dots button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Verify delete note link under three dots button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify delete note link under three dots button"


@then(u'Click save button on edit a note')
def click_save_btn_on_edit_a_note(context):
    try:
       context.DashboardPage.click_save_btn_on_edit_a_note()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e) + "Test Failed on Click save button on edit a note"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str("Test Failed on Click save button on edit a note"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click save button on edit a note"


@then(u'Choose location from location input field on add note popup window add note and click on save button')
def verify_select_location_from_location_input_field_on_add_note_popup_window_add_note_and_click_on_save_button(context):
    try:
        global note
        note = context.BasePage.generate_random_data_against_a_keyword('Note')
        context.DashboardPage.select_location_from_location_input_field_on_add_note_popup_window()
        context.DashboardPage.add_note_on_add_a_new_note_popup_window(note)
        context.DashboardPage.click_save_btn_on_edit_a_note()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify select location from location input field on add note popup window add note and click on save button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Verify select location from location input field on add note popup window add note and click on save button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify select location from location input field on add note popup window add note and click on save button"


@then(u'Verify edit habit note popup window "{value}"')
def verify_edit_habit_note_popup_window(context, value):
    try:
        if value == 'displaying':
            context.DashboardPage.verify_edit_habit_note_popup_window()
        else:
            if not context.DashboardPage.verify_edit_habit_note_popup_window():
                return True
            else:
                return False

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify edit habit note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Verify edit habit note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Verify edit habit note popup window"

@then(u'Click save button on edit a new note popup window')
def click_save_btn_on_edit_a_note(context):
    try:
        context.DashboardPage.click_save_btn_on_edit_a_note()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Click save button on edit a new note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Click save button on edit a new note popup window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click save button on edit a new note popup window"

@then(u'Please select location message "{value}"')
def verify_please_select_location_message(context, value):
    try:
        if value == 'displaying':
            context.DashboardPage.verify_please_select_location_message()
        else:
            if not context.DashboardPage.verify_please_select_location_message():
                return True
            else:
                return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Please select location message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Please select location message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Please select location message"

@then(u'Enter add note popup window add note and click on add button')
def verify_select_location_from_location_input_field_on_add_note_popup_window_add_note_and_click_on_add_button(context):
    try:
        global note
        note = context.BasePage.generate_random_data_against_a_keyword('Note')
        context.DashboardPage.add_note_on_add_a_new_note_popup_window(note)
        context.DashboardPage.click_add_btn_on_add_a_new_note_popup_window()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Enter add note popup window add note and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Enter add note popup window add note and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Enter add note popup window add note and click on add button"

@then(u'Please enter note message "{value}"')
def verify_please_enter_note_message(context, value):
    try:
        if value == 'displaying':
            context.DashboardPage.verify_please_enter_note_message()
        else:
            if not context.DashboardPage.verify_please_enter_note_message():
                return True
            else:
                return False
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Please enter note message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Please enter note message"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Please enter note message"

@then(u'Choose location from location input field and click on add button')
def verify_select_location_from_location_input_field_on_add_note_popup_window_and_click_on_add_button(context):
    try:
        context.DashboardPage.select_location_from_location_input_field_on_add_note_popup_window()
        context.DashboardPage.click_add_btn_on_add_a_new_note_popup_window()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Choose location from location input field and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Choose location from location input field and click on add button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Choose location from location input field and click on add button"


@then(u'Choose location from location input field, clear note field and click on save button')
def verify_select_location_clear_note_field_on_add_note_popup_window_and_click_on_save_button(context):
    try:
        context.DashboardPage.clear_note_field_on_add_a_new_note_popup_window()
        context.DashboardPage.select_location_from_location_input_field_on_add_note_popup_window()
        context.DashboardPage.click_save_btn_on_edit_a_note()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Choose location from location input field, clear note field and click on save button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Choose location from location input field, clear note field and click on save button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Choose location from location input field, clear note field and click on save button"

@then(u'Verify delete note pop up "{value}"')
def verify_delete_note_popup_window(context, value):
    try:
        if value == 'displaying':
            context.DashboardPage.verify_delete_note_popup_window()
        else:
            if not context.DashboardPage.verify_delete_note_popup_window():
                return True
            else:
                return False

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify delete note pop up"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Click delete button on delete note pop up')
def click_on_delete_btn_on_delete_note_popup_window(context):
    try:
        context.DashboardPage.click_on_delete_btn_on_delete_note_popup_window()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on Verify delete button on delete note pop up"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

    except:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   "Test Failed on Click delete button on delete note pop up"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Click delete button on delete note pop up"

@then(u'Click x icon on delete note pop up window')
def click_x_icon_on_delete_popup_window(context):
    try:
        context.DashboardPage.click_x_icon_on_delete_popup_window()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on click x icon on delete note pop up window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click close button on delete note pop up window')
def click_close_button_on_delete_popup_window(context):
    try:
        context.DashboardPage.click_close_button_on_delete_popup_window()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(
                   str(e) + "Test Failed on click close button on delete note pop up window"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


