import typing

from FactionChain import FactionChain
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionChainsResponse(BaseSchema):

    chains: typing.List[FactionChain]
    _metadata: RequestMetadataWithLinks
