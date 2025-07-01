import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_track import RaceTrack


@dataclass
class RacingTracksResponse(BaseSchema):
    """
    JSON object of `RacingTracksResponse`.
    """

    tracks: typing.List[RaceTrack]

    @staticmethod
    def parse(data):
        return RacingTracksResponse(
            tracks=BaseSchema.parse(data.get("tracks"), typing.List[RaceTrack]),
        )
