import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class MarketHistoryEntry(BaseSchema):
    """
    JSON object of `MarketHistoryEntry`.
    """

    timestamp: int
    price: None | int
    circulation: None | int

    @staticmethod
    def parse(data):
        return MarketHistoryEntry(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            price=BaseSchema.parse(data.get("price"), None | int),
            circulation=BaseSchema.parse(data.get("circulation"), None | int),
        )
