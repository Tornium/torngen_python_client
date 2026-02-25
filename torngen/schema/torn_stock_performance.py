import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornStockPerformance(BaseSchema):
    """
    JSON object of `TornStockPerformance`.
    """

    start: int | float
    low: int | float
    high: int | float
    end: int | float
    change_percentage: int | float
    change: int | float

    @staticmethod
    def parse(data):
        return TornStockPerformance(
            start=BaseSchema.parse(data.get("start"), int | float),
            low=BaseSchema.parse(data.get("low"), int | float),
            high=BaseSchema.parse(data.get("high"), int | float),
            end=BaseSchema.parse(data.get("end"), int | float),
            change_percentage=BaseSchema.parse(
                data.get("change_percentage"), int | float
            ),
            change=BaseSchema.parse(data.get("change"), int | float),
        )
