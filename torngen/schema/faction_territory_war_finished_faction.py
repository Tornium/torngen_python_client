import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionTerritoryWarFinishedFaction(BaseSchema):
    """
    JSON object of `FactionTerritoryWarFinishedFaction`.
    """

    score: int
    name: str
    is_aggressor: bool
    id: FactionId

    @staticmethod
    def parse(data):
        return FactionTerritoryWarFinishedFaction(
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_aggressor=BaseSchema.parse(data.get("is_aggressor"), bool),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )
