import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_chain_warfare import FactionChainWarfare
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionWarfareChainsResponse(BaseSchema):
    """
    JSON object of `FactionWarfareChainsResponse`.
    """

    warfarechains: typing.List[FactionChainWarfare]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionWarfareChainsResponse(
            warfarechains=BaseSchema.parse(
                data.get("warfarechains"), typing.List[FactionChainWarfare]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
