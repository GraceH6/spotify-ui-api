import pytest

from utils.api_requests import ApiRequests
from utils.constants.test_data import Singers, Genres


class TestAPI:
    api_requests: ApiRequests = ApiRequests()
    token = api_requests.get_token()

    @pytest.mark.parametrize(
        "singer_name, genre",
        [
            pytest.param(Singers.DRAKE, Genres.RAP.lower()),
            pytest.param(Singers.THE_BEATLES, Genres.BRITISH_INVASION.lower())
        ]
    )
    def test_spotify_api(self, singer_name: str, genre: str):
        artist_data = self.api_requests.get_artist(singer_name, self.token)
        print(artist_data)
        assert genre in artist_data.artists.items[0].genres, f"A genre called '{genre}' should exist"
