import typing

from FactionRankedWarDetails import FactionRankedWarDetails
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionRankedWarResponse(BaseSchema):

    rankedwars: typing.List[FactionRankedWarDetails]
    _metadata: RequestMetadataWithLinks
