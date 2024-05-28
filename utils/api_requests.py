import os
import requests

from dotenv import load_dotenv
from utils.constants.spotify_constants import ApiEndpoints
from base64 import b64encode


class ApiRequests:
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    def get_token(self):
        token_url = ApiEndpoints.TOKEN_ENDPOINT

        headers = {
            "Authorization": "Basic " + b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode(),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }
        response = requests.post(token_url, headers=headers, data=data)
        response_data = response.json()

        return response_data["access_token"]

    def get_artist(self, artist_name, token):
        search_url = ApiEndpoints.SEARCH_API_URL

        headers = {
            "Authorization": f"Bearer {token}"
        }
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 1
        }
        response = requests.get(search_url, headers=headers, params=params)

        return response

    def get_artist_top_tracks(self, artist_id, token):
        top_tracks_url = f"{ApiEndpoints.BASE_API_URL}/artists/{artist_id}{ApiEndpoints.TOP_TRACKS_ENDPOINT}"

        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url=top_tracks_url, headers=headers)

        return response
