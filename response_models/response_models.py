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


class TrackItem(BaseModel):
    name: str
    popularity: int
    href: HttpUrl
    id: str
    uri: str


class TopTracks(BaseModel):
    tracks: List[TrackItem]


class ArtistsResponse(BaseModel):
    artists: Artists
    top_tracks: Optional[TopTracks]
