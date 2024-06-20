from selenium.webdriver.common.by import By
from amazon_minitv_test.pages.base_page import BasePage


class SeriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.particular_season = "//android.widget.Spinner[contains(@text, '%season_name%')]"
        self.seasons_dropdown = (By.XPATH, "//android.widget.Spinner[contains(@text, 'Season')]")
        self.seasons_list = (By.XPATH, "//android.widget.TextView[contains(@text, 'Season')]")
        self.first_episode = (By.XPATH, "//android.widget.TextView[contains(@text, '1.')]")
        self.playback_status_play = (By.XPATH, "//android.widget.ImageView[@content-desc='Pause']")
        self.playback_status_pause = (By.XPATH, "//android.widget.ImageView[@content-desc='Play']")
        self.series_name_series_page = (By.XPATH, "//android.widget.ImageView[@text, 'series_name']")

    def click_seasons_dropdown(self):
        self.click(self.seasons_dropdown)

    def get_all_seasons(self):
        self.click_seasons_dropdown()
        season_names = []
        seasons = self.driver.find_elements(*self.seasons_list)
        for season in seasons:
            season_names.append(self.get_text(season))
        return season_names

    def open_season_of_series(self, season_name):
        self.click_seasons_dropdown()
        particular_season = self.particular_season.replace("%season_name%", season_name)
        season_element = self.driver.find_element(By.XPATH, particular_season)
        season_element.click()

    def play_first_episode(self):
        self.click(self.first_episode)

    def is_video_playing(self):
        assert not self.is_displayed(self.playback_status_pause), "Still the video is on pause mode"
        return self.is_displayed(self.playback_status_play)

    def get_series_name(self):
        return self.get_text(self.series_name_series_page)