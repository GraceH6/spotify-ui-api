import pytest
from playwright.sync_api import Page, expect
from utils.constants.test_data import Singers, Songs
from utils.constants.spotify_constants import SpotifyUIUrl
from spotify_forms.left_nav_form import LeftNavigationForm
from spotify_forms.main_form import MainContentForm


class TestSpotifyUI:

    left_nav_form: LeftNavigationForm = LeftNavigationForm()
    main_form: MainContentForm = MainContentForm()

    @pytest.mark.parametrize(
        "singer_name, expected_song",
        [
            pytest.param(Singers.DRAKE, Songs.ONE_DANCE),
            pytest.param(Singers.THE_BEATLES, Songs.HERE_COMES_THE_SUN)
        ]
    )
    def test_singers_songs(self, page: Page, singer_name, expected_song):
        page.goto(SpotifyUIUrl.BASE_UI_URL)
        self.left_nav_form.click_search_btn(page)
        self.main_form.search_singer(page, singer_name)
        expect(self.main_form.get_song_by_name(page, expected_song)).to_be_visible()
