import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class HofValueFloat(BaseSchema):
    """
    JSON object of `HofValueFloat`.
    """

    value: int | float
    rank: int

    @staticmethod
    def parse(data):
        return HofValueFloat(
            value=BaseSchema.parse(data.get("value"), int | float),
            rank=BaseSchema.parse(data.get("rank"), int),
        )
