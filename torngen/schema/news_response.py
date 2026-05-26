import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .news import News
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class NewsResponse(BaseSchema):
    """
    JSON object of `NewsResponse`.
    """

    news: typing.List[News]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return NewsResponse(
            news=BaseSchema.parse(data.get("news"), typing.List[News]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
