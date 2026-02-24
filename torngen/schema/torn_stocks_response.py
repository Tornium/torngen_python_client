import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_stock import TornStock


@dataclass
class TornStocksResponse(BaseSchema):
    """
    JSON object of `TornStocksResponse`.
    """

    stocks: typing.List[TornStock]

    @staticmethod
    def parse(data):
        return TornStocksResponse(
            stocks=BaseSchema.parse(data.get("stocks"), typing.List[TornStock]),
        )
