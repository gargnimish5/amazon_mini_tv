from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from amazon_minitv_test.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_tab = (By.ID, "com.amazon.mShop.android.shopping:id/rs_search_src_text")
        self.search_tab_box = "com.amazon.mShop.android.shopping:id/rs_search_src_text_box"
        self.first_search_result = (By.XPATH, "//android.widget.TextView[contains(@text, '%seriesName%')][0]")
        self.series_description = (By.ID, "com.amazon.mShop.android.shopping:id/some_description_id")

    def search_series(self, series_name):
        self.click(self.search_tab)
        self.send_keys(self.search_tab_box, series_name)
        self.send_keys(self.search_tab_box, Keys.ENTER)

    def select_first_search_result(self, series_name):
        search_tab_box = self.search_tab_box.replace("%seriesName%", series_name)
        self.click((By.ID, search_tab_box))

