import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornBank(BaseSchema):
    """
    JSON object of `TornBank`.
    """

    rate: int | float
    days: int

    @staticmethod
    def parse(data):
        return TornBank(
            rate=BaseSchema.parse(data.get("rate"), int | float),
            days=BaseSchema.parse(data.get("days"), int),
        )
