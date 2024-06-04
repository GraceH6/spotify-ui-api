import pytest
from playwright.sync_api import expect
from utils.constants.test_data import Singers, Songs
from utils.constants.spotify_constants import SpotifyUIUrl
from spotify_forms.left_nav_form import LeftNavigationForm
from spotify_forms.main_form import MainContentForm
from utils.page_instance import SingletonPage


class TestSpotifyUI:

    __page = SingletonPage().get_page()
    __left_nav_form: LeftNavigationForm = LeftNavigationForm()
    __main_form: MainContentForm = MainContentForm()

    @pytest.mark.parametrize(
        "singer_name, expected_song",
        [
            pytest.param(Singers.DRAKE, Songs.ONE_DANCE),
            pytest.param(Singers.THE_BEATLES, Songs.HERE_COMES_THE_SUN)
        ]
    )
    def test_singers_songs(self, singer_name, expected_song):
        self.__page.goto(SpotifyUIUrl.BASE_UI_URL)
        self.__left_nav_form.click_search_btn()
        self.__main_form.search_singer(singer_name)
        expect(self.__main_form.get_song_by_name(expected_song)).to_be_visible()
