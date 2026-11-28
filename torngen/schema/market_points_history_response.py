import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_history_entry import MarketHistoryEntry
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class MarketPointsHistoryResponse(BaseSchema):
    """
    JSON object of `MarketPointsHistoryResponse`.
    """

    pointshistory: typing.List[MarketHistoryEntry]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return MarketPointsHistoryResponse(
            pointshistory=BaseSchema.parse(
                data.get("pointshistory"), typing.List[MarketHistoryEntry]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
