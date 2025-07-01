import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_search import FactionSearch
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionSearchResponse(BaseSchema):
    """
    JSON object of `FactionSearchResponse`.
    """

    search: typing.List[FactionSearch]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionSearchResponse(
            search=BaseSchema.parse(data.get("search"), typing.List[FactionSearch]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
