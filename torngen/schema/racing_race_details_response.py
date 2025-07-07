import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .racing_race_details import RacingRaceDetails


@dataclass
class RacingRaceDetailsResponse(BaseSchema):
    """
    JSON object of `RacingRaceDetailsResponse`.
    """

    race: RacingRaceDetails

    @staticmethod
    def parse(data):
        return RacingRaceDetailsResponse(
            race=BaseSchema.parse(data.get("race"), RacingRaceDetails),
        )
