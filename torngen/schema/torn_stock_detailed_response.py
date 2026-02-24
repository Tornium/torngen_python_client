import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_stock_detailed import TornStockDetailed


@dataclass
class TornStockDetailedResponse(BaseSchema):
    """
    JSON object of `TornStockDetailedResponse`.
    """

    stocks: TornStockDetailed

    @staticmethod
    def parse(data):
        return TornStockDetailedResponse(
            stocks=BaseSchema.parse(data.get("stocks"), TornStockDetailed),
        )
