import pytest
from amazon_minitv_test.pages.home_tab import HomePage
from amazon_minitv_test.pages.search_tab import SearchPage
from amazon_minitv_test.pages.series_page import SeriesPage
from amazon_minitv_test.config import properties as prop


@pytest.mark.usefixtures("driver")
class TestAmazonMiniTVPlayback:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.search_page = SearchPage(driver)
        self.series_page = SeriesPage(driver)

    def test_home_page_displayed(self):
        assert self.home_page.is_home_page_displayed(), "Home page logo is not displayed"

    def test_search_series(self):
        self.search_page.search_series(prop.series_name)
        self.search_page.select_first_search_result(prop.series_name)
        series_name_on_page = self.series_page.get_series_name()
        assert prop.series_name in series_name_on_page, f"Series Name series page does not match for {prop.series_name}"

    def test_play_first_episode_of_each_season(self):
        season_names = self.series_page.get_all_seasons()
        assert len(season_names) > 0, "No seasons found"

        for season in season_names:
            self.series_page.open_season_of_series(season)
            self.series_page.play_first_episode()
            assert self.series_page.is_video_playing(), f"Video is not playing for {season}"

