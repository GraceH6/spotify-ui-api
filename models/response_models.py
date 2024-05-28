from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class ExternalUrls(BaseModel):
    spotify: HttpUrl


class Followers(BaseModel):
    href: Optional[str]
    total: int


class Image(BaseModel):
    height: int
    url: HttpUrl
    width: int


class ArtistItem(BaseModel):
    external_urls: ExternalUrls
    followers: Followers
    genres: List[str]
    href: HttpUrl
    id: str
    images: List[Image]
    name: str
    popularity: int
    type: str
    uri: str


class Artists(BaseModel):
    href: HttpUrl
    items: List[ArtistItem]
    limit: int
    next: Optional[HttpUrl]
    offset: int
    previous: Optional[str]
    total: int


class ArtistsResponse(BaseModel):
    artists: Artists


class TopTracksResponse:
    def __init__(self, tracks):
        self.tracks = [Track(**track) for track in tracks]


class Track:
    def __init__(self, album, artists, available_markets, disc_number, duration_ms, explicit, external_ids,
                 external_urls, href, id, is_local, name, popularity, preview_url, track_number, type, uri):
        self.album = Album(**album)
        self.artists = [Artist(**artist) for artist in artists]
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = ExternalIDs(**external_ids)
        self.external_urls = ExternalURLs(**external_urls)
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri


class Album:
    def __init__(self, album_type, artists, available_markets, external_urls, href, id, images, name, release_date,
                 release_date_precision, total_tracks, type, uri):
        self.album_type = album_type
        self.artists = [Artist(**artist) for artist in artists]
        self.available_markets = available_markets
        self.external_urls = ExternalURLs(**external_urls)
        self.href = href
        self.id = id
        self.images = [Image(**image) for image in images]
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.total_tracks = total_tracks
        self.type = type
        self.uri = uri


class Artist:
    def __init__(self, external_urls, href, id, name, type, uri):
        self.external_urls = ExternalURLs(**external_urls)
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri


class ExternalURLs:
    def __init__(self, spotify):
        self.spotify = spotify


class Image:
    def __init__(self, height, url, width):
        self.height = height
        self.url = url
        self.width = width


class ExternalIDs:
    def __init__(self, isrc):
        self.isrc = isrc
