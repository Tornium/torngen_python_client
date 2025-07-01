import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class HofValue(BaseSchema):
    """
    JSON object of `HofValue`.
    """

    value: int
    rank: int

    @staticmethod
    def parse(data):
        return HofValue(
            value=BaseSchema.parse(data.get("value"), int),
            rank=BaseSchema.parse(data.get("rank"), int),
        )
