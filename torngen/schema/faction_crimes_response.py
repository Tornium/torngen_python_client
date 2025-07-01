import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionCrimesResponse(BaseSchema):
    """
    JSON object of `FactionCrimesResponse`.
    """

    crimes: typing.List[FactionCrime]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionCrimesResponse(
            crimes=BaseSchema.parse(data.get("crimes"), typing.List[FactionCrime]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
