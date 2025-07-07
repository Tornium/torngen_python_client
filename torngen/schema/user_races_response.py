import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .racing_race_details import RacingRaceDetails
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class UserRacesResponse(BaseSchema):
    """
    JSON object of `UserRacesResponse`.
    """

    races: typing.List[RacingRaceDetails]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserRacesResponse(
            races=BaseSchema.parse(data.get("races"), typing.List[RacingRaceDetails]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
