import pytest

from utils.api_requests import ApiRequests
from utils.constants.test_data import Singers, Genres, Songs
from models.response_models import ArtistsResponse, TopTracksResponse


class TestAPI:
    api_requests: ApiRequests = ApiRequests()
    token = api_requests.get_token()

    @pytest.mark.parametrize(
        "singer_name, expected_genre",
        [
            pytest.param(Singers.DRAKE, Genres.RAP.lower()),
            pytest.param(Singers.THE_BEATLES, Genres.BRITISH_INVASION.lower())
        ]
    )
    def test_spotify_api(self, singer_name: str, expected_genre: str):
        response = self.api_requests.get_artist(singer_name, self.token)

        assert response.status_code == 200

        response_data = response.json()
        artist_data = ArtistsResponse(**response_data)

        assert expected_genre in artist_data.artists.items[0].genres, f"A genre called '{expected_genre}' should exist"

    @pytest.mark.parametrize(
        "singer_name, expected_song",
        [
            pytest.param(Singers.DRAKE, Songs.ONE_DANCE),
            pytest.param(Singers.THE_BEATLES, Songs.HERE_COMES_THE_SUN)
        ]
    )
    def test_is_song_popular(self, singer_name, expected_song):
        artist_response = self.api_requests.get_artist(singer_name, self.token).json()
        artist_id = ArtistsResponse(**artist_response).artists.items[0].id

        response = self.api_requests.get_artist_top_tracks(artist_id, self.token)

        assert response.status_code == 200

        top_tracks_data = TopTracksResponse(**response.json())

        found = False

        for track in top_tracks_data.tracks:
            if track.name == expected_song:
                found = True
                print(track.name)
                break

        assert found, f"A song named '{expected_song}' should be among popular ones"
