class ApiEndpoints:
    BASE_API_URL: str = "https://api.spotify.com/v1"
    TOKEN_ENDPOINT: str = "https://accounts.spotify.com/api/token"
    SEARCH_API_URL: str = f"{BASE_API_URL}/search"
    ARTISTS_ENDPOINT: str = f"{BASE_API_URL}/artists"
    TOP_TRACKS_ENDPOINT: str = "/top-tracks"


class SpotifyUIUrl:
    BASE_UI_URL: str = "https://open.spotify.com/"
