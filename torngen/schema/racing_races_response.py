import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race import Race
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class RacingRacesResponse(BaseSchema):
    """
    JSON object of `RacingRacesResponse`.
    """

    races: typing.List[Race]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return RacingRacesResponse(
            races=BaseSchema.parse(data.get("races"), typing.List[Race]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
