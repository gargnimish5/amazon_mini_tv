import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from amazon_minitv_test.config import properties as prop

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = prop.platform_name
    options.device_name = prop.device_name
    options.automation_name = prop.automation_name
    options.app_package = prop.app_package
    options.app_activity = prop.app_activity

    driver = webdriver.Remote(prop.appium_url, options=options)
    yield driver
    driver.quit()