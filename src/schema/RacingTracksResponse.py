import typing

from RaceTrack import RaceTrack

from ..base_schema import BaseSchema


class RacingTracksResponse(BaseSchema):

    tracks: typing.List[RaceTrack]
