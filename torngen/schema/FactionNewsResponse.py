import typing

from FactionNews import FactionNews
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionNewsResponse(BaseSchema):

    news: typing.List[FactionNews]
    _metadata: RequestMetadataWithLinks
