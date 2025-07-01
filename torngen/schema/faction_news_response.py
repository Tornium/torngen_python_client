import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_news import FactionNews
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionNewsResponse(BaseSchema):
    """
    JSON object of `FactionNewsResponse`.
    """

    news: typing.List[FactionNews]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionNewsResponse(
            news=BaseSchema.parse(data.get("news"), typing.List[FactionNews]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
