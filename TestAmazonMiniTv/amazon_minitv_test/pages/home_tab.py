from selenium.webdriver.common.by import By
from amazon_minitv_test.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.app_logo = (By.XPATH, "miniTv")

    def is_home_page_displayed(self):
        return self.is_displayed(self.app_logo)
