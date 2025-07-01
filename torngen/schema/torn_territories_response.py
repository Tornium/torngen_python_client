import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .torn_territory import TornTerritory


@dataclass
class TornTerritoriesResponse(BaseSchema):
    """
    JSON object of `TornTerritoriesResponse`.
    """

    territory: typing.List[TornTerritory]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornTerritoriesResponse(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[TornTerritory]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
