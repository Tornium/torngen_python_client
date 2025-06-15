import typing

from Bounty import Bounty
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class TornBountiesResponse(BaseSchema):

    bounties: typing.List[Bounty]
    _metadata: RequestMetadataWithLinks
