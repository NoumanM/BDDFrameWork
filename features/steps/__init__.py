import os
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Constants.config import TestData
from Constants.config import userdata
from pages.LoginPage import LoginPage
from pages.BasePage import BasePage
from pages.SignupPage import SignupPage
from pages.ForgetPasswordPage import ForgetPasswordPage
from pages.DashboardPage import DashboardPage
from pages.AddNewCategoryPage import AddNewCategoryPage
from pages.ProfilePage import ProfilePage
from pages.LogoutPage import LogoutPage
from pages.AnalyticsPage import AnalyticsPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path

home_directory = Path(__file__).resolve().parent.parent.parent

@given(u'Launch the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": f"{home_directory}\TestData",
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("prefs", prefs)
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        if TestData.PLATFORM == 'Browser Stack':
            desired_cap ={
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Firefox',
            'browser_version': '90.0',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
            }
            context.driver = webdriver.Remote(
            command_executor = 'https://{User_name}:{Key}@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities = desired_cap)
        elif TestData.PLATFORM == 'local':
            context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            #context.driver = webdriver.Chrome(executable_path=r"C:\Users\CodeAutomation\Desktop\hat-web\drivers\chromedriver.exe", options=options)
        elif TestData.PLATFORM == 'Docker':
            remote_url = os.getenv('SELENIUM_GRID_URL')
            time.sleep(5)
            context.driver = webdriver.Remote(command_executor=f'http://{remote_url}/wd/hub',
            desired_capabilities = DesiredCapabilities.CHROME, options = options)
        context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


@when(u'Open the website_url')
def open_login_page(context):
    try:
        context.driver.get(userdata.url)
        context.loginPage = LoginPage(context.driver)
        context.SignupPage = SignupPage(context.driver)
        context.ForgetPasswordPage = ForgetPasswordPage(context.driver)
        context.DashboardPage = DashboardPage(context.driver)
        context.BasePage = BasePage(context.driver)
        context.AddNewCategoryPage = AddNewCategoryPage(context.driver)
        context.ProfilePage = ProfilePage(context.driver)
        context.LogoutPage = LogoutPage(context.driver)
        context.AnalyticsPage = AnalyticsPage(context.driver)
    except Exception as e:
        print(e)
        context.driver.close()
        assert False, "Test is failed in open section"
