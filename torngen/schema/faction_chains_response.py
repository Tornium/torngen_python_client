import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_chain import FactionChain
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionChainsResponse(BaseSchema):
    """
    JSON object of `FactionChainsResponse`.
    """

    chains: typing.List[FactionChain]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionChainsResponse(
            chains=BaseSchema.parse(data.get("chains"), typing.List[FactionChain]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
