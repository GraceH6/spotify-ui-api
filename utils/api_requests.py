from dotenv import load_dotenv
from utils.constants.api_constants import Endpoints
from base64 import b64encode
from response_models.response_models import ArtistsResponse, TopTracks
import os
import requests


class ApiRequests:
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    def get_token(self):
        token_url = Endpoints.TOKEN_ENDPOINT

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
        search_url = Endpoints.SEARCH_API_URL
        headers = {
            "Authorization": f"Bearer {token}"
        }
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 1
        }

        response = requests.get(search_url, headers=headers, params=params)
        response_data = response.json()
        artist_data = ArtistsResponse(**response_data)

        return artist_data
