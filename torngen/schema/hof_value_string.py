import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class HofValueString(BaseSchema):
    """
    JSON object of `HofValueString`.
    """

    value: str
    rank: None | int

    @staticmethod
    def parse(data):
        return HofValueString(
            value=BaseSchema.parse(data.get("value"), str),
            rank=BaseSchema.parse(data.get("rank"), None | int),
        )
