import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionRaidWarfareFaction(BaseSchema):
    """
    JSON object of `FactionRaidWarfareFaction`.
    """

    score: int | float
    name: str
    id: FactionId
    chain: int

    @staticmethod
    def parse(data):
        return FactionRaidWarfareFaction(
            score=BaseSchema.parse(data.get("score"), int | float),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            chain=BaseSchema.parse(data.get("chain"), int),
        )
