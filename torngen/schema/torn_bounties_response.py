import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bounty import Bounty
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class TornBountiesResponse(BaseSchema):
    """
    JSON object of `TornBountiesResponse`.
    """

    bounties: typing.List[Bounty]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornBountiesResponse(
            bounties=BaseSchema.parse(data.get("bounties"), typing.List[Bounty]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
