import typing

from RaceTrackId import RaceTrackId

from ..base_schema import BaseSchema


class RaceTrack(BaseSchema):

    title: str
    id: RaceTrackId
    description: str
