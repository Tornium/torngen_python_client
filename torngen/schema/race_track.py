import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_track_id import RaceTrackId


@dataclass
class RaceTrack(BaseSchema):
    """
    JSON object of `RaceTrack`.
    """

    title: str
    id: RaceTrackId
    description: str

    @staticmethod
    def parse(data):
        return RaceTrack(
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), RaceTrackId),
            description=BaseSchema.parse(data.get("description"), str),
        )
