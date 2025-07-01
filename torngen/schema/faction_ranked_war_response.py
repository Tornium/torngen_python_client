import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_ranked_war_details import FactionRankedWarDetails
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionRankedWarResponse(BaseSchema):
    """
    JSON object of `FactionRankedWarResponse`.
    """

    rankedwars: typing.List[FactionRankedWarDetails]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionRankedWarResponse(
            rankedwars=BaseSchema.parse(
                data.get("rankedwars"), typing.List[FactionRankedWarDetails]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
