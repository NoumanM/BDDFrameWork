from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *


@then(u'Click analytics button')
def click_analytics_btn(context):
    try:
        context.AnalyticsPage.click_analytics_btn()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify analytics button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify charts, net worth, stats tab on analytics page')
def verify_charts_net_worth_stats_tab(context):
    try:
        context.AnalyticsPage.verify_net_worth_tab()
        context.AnalyticsPage.verify_charts_tab()
        context.AnalyticsPage.verify_stats_tab()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify analytics button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click net worth tab')
def click_net_worth_tab(context):
    try:
        context.AnalyticsPage.click_net_worth_tab()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click net worth tab"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click charts tab')
def click_charts_tab(context):
    try:
        context.AnalyticsPage.click_charts_tab()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click charts tab"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click Stats tab')
def click_stats_tab(context):
    try:
        context.AnalyticsPage.click_stats_tab()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click stats tab"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify net worth label')
def verify_net_worth_label(context):
    try:
        context.AnalyticsPage.verify_net_worth_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify net worth label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Verify area activity tracker label')
def verify_area_activity_tracker_label(context):
    try:
        context.AnalyticsPage.verify_area_activity_tracker_label()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify area activity tracker label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Select date on net worth page to and from')
def select_to_and_from_date_on_net_worth_calendar(context):
    try:
        context.AnalyticsPage.select_to_and_from_date_on_net_worth_calendar()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Select date on net worth page to and from"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify balance as of starting date, ending date, Net Income and Net Returns')
def select_to_and_from_date_on_net_worth_calendar(context):
    try:
        context.AnalyticsPage.verify_balance_as_of_starting_date()
        context.AnalyticsPage.verify_balance_as_of_end_date()
        context.AnalyticsPage.verify_net_income()
        context.AnalyticsPage.verify_net_returns()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify balance as of starting date, ending date, Net Income and Net Returns"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify the row names under stats')
@then(u'Verify the row names under net worth')
def row_under_net_worth(context):
    try:
        names = context.AnalyticsPage.get_row_under_net_worth()
        for val in names:
            attach(val,
                   name="Value under net worth",
                   attachment_type=AttachmentType.TEXT)

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify the row names under net worth"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify asset liabilities gain/loss and returns label')
def verify_asset_liabilities_gain_loss_and_return_labels(context):
    try:
         context.AnalyticsPage.verify_asset_liabilities_gain_loss_and_return_labels()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify asset liabilities gain/loss and returns label"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click export to excel button')
def click_export_to_excel_btn(context):
    try:
         context.AnalyticsPage.click_export_to_excel_btn()

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click export to excel button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify the download file')
def verify_file_exist_or_not(context):
    try:
         context.AnalyticsPage.verify_file_exist_or_not()
         context.AnalyticsPage.delete_the_download_file()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify the download file"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify tracking week label, next and previous button')
def verify_tracking_week_label_next_and_previous_btns(context):
    try:
         context.AnalyticsPage.verify_tracking_week_label_next_and_previous_btns()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify tracking week label, next and previous button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Verify area comparison chart')
def verify_area_comparison_chart(context):
    try:
         context.AnalyticsPage.verify_area_comparison_chart()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify area comparison chart"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify weekly comparison chart')
def verify_weekly_comparison_chart(context):
    try:
         context.AnalyticsPage.verify_weekly_comparison_chart()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify weekly comparison chart"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify area activity tracker and elements under it')
def verify_area_activity_tracker(context):
    try:
         context.AnalyticsPage.verify_area_activity_tracker()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify area activity tracker and elements under it"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click date picker under tracking week')
def click_date_picker_under_tracking_week(context):
    try:
         context.AnalyticsPage.click_date_picker_under_tracking_week()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click date picker under tracking week"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Click tracking year dropdown')
def click_tracking_year_dropdown(context):
    try:
         context.AnalyticsPage.click_tracking_year_dropdown()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click date picker under tracking week"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Click start year 2022')
def click_start_year_2022(context):
    try:
         context.AnalyticsPage.click_start_year_2022()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Click start year 2022"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e


@then(u'Verify previous years are disabled')
def verify_previous_years_are_disabled(context):
    try:
         context.AnalyticsPage.verify_previous_years_are_disabled()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify previous years are disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify element color')
def verify_element_color(context):
    try:
         context.AnalyticsPage.click_tracking_year_dropdown()
         value = context.AnalyticsPage.verify_element_color()
         attach(value,
                name="Selected element color",
                attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify previous years are disabled"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify modify view and export to excel button')
def verify_export_to_excel_btn_and_modify_view(context):
    try:
         context.AnalyticsPage.verify_export_to_excel_btn()
         context.AnalyticsPage.verify_modify_view_btn_on_stats()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify modify view and export to excel button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify the color of modify view button after hovering')
def verify_modify_view_color(context):
    try:
         value = context.AnalyticsPage.verify_color_after_hovering_over_modify_view()
         attach(value,
                name="Selected element color",
                attachment_type=AttachmentType.TEXT)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify the color of modify view button after hovering"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e

@then(u'Verify the points infront of each category')
def row_under_net_worth(context):
    try:
        names = context.AnalyticsPage.get_points_infront_of_each_category()
        for val in names:
            attach(val,
                   name="Value under net worth",
                   attachment_type=AttachmentType.TEXT)

    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(str(e)+"Test Failed on Verify the points infront of each category"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e