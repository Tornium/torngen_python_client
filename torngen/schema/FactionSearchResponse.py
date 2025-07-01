import typing

from FactionSearch import FactionSearch
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionSearchResponse(BaseSchema):

    search: typing.List[FactionSearch]
    _metadata: RequestMetadataWithLinks
