import pytest

from conftest import browser
from spotify_forms.left_nav_form import LeftNavigationForm
from spotify_forms.main_form import MainContentForm
from utils.constants.spotify_constants import SpotifyUIUrl
from utils.constants.test_data import Singers, Songs


class TestSpotifyUI:
    left_nav_form: LeftNavigationForm = LeftNavigationForm()

    @pytest.mark.parametrize(
        "singer_name, expected_song",
        [
            pytest.param(Singers.DRAKE, Songs.ONE_DANCE),
            pytest.param(Singers.THE_BEATLES, Songs.HERE_COMES_THE_SUN)
        ]
    )
    def test_search_song(self, browser, singer_name: str, expected_song: str):
        browser.go_to(url=SpotifyUIUrl.BASE_UI_URL)

        self.left_nav_form.click_search_btn()

        main_form = MainContentForm()
        main_form.search_singer(singer_name)

        assert main_form.get_song_by_name(expected_song).text == expected_song, \
            f"A song named '{expected_song}' should be present"
