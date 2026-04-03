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

    bounties_timestamp: int
    bounties_delay: typing.Optional[int]
    bounties: typing.List[Bounty]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornBountiesResponse(
            bounties_timestamp=BaseSchema.parse(data.get("bounties_timestamp"), int),
            bounties_delay=BaseSchema.parse(
                data.get("bounties_delay"), typing.Optional[int]
            ),
            bounties=BaseSchema.parse(data.get("bounties"), typing.List[Bounty]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
