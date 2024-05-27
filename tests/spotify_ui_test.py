import time
import pytest

from conftest import browser
from spotify_forms.left_nav_form import LeftNavigationForm
from spotify_forms.main_form import MainContentForm
from utils.constants.url_constants import SpotifyUrl
from utils.constants.test_data import SingersAndSongs


class TestSpotifyUI:
    left_nav_form: LeftNavigationForm = LeftNavigationForm()

    @pytest.mark.parametrize(
        "singer_name, song",
        [
            pytest.param(SingersAndSongs.DRAKE, SingersAndSongs.ONE_DANCE_SONG),
            pytest.param(SingersAndSongs.THE_BEATLES, SingersAndSongs.HERE_COMES_THE_SUN_SONG)
        ]
    )
    def test_search_song(self, browser, singer_name: str, song: str):
        browser.go_to(url=SpotifyUrl.SPOTIFY_URL)

        self.left_nav_form.click_search_btn()

        main_form = MainContentForm()
        main_form.search_singer(singer_name)

        assert main_form.get_song_by_name(song).text == song, f"A song named '{song}' should be present"
