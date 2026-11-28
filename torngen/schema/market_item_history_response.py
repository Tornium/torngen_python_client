import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_history_entry import MarketHistoryEntry
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class MarketItemHistoryResponse(BaseSchema):
    """
    JSON object of `MarketItemHistoryResponse`.
    """

    itemhistory: typing.List[MarketHistoryEntry]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return MarketItemHistoryResponse(
            itemhistory=BaseSchema.parse(
                data.get("itemhistory"), typing.List[MarketHistoryEntry]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
