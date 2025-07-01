import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionRank(BaseSchema):
    """
    JSON object of `FactionRank`.
    """

    wins: int
    position: int
    name: str
    level: int
    division: int

    @staticmethod
    def parse(data):
        return FactionRank(
            wins=BaseSchema.parse(data.get("wins"), int),
            position=BaseSchema.parse(data.get("position"), int),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            division=BaseSchema.parse(data.get("division"), int),
        )
