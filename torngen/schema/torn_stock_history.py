import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornStockHistory(BaseSchema):
    """
    JSON object of `TornStockHistory`.
    """

    timestamp: int
    price: int | float
    change: int | float

    @staticmethod
    def parse(data):
        return TornStockHistory(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            price=BaseSchema.parse(data.get("price"), int | float),
            change=BaseSchema.parse(data.get("change"), int | float),
        )
