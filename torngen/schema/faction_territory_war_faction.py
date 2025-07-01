import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionTerritoryWarFaction(BaseSchema):
    """
    JSON object of `FactionTerritoryWarFaction`.
    """

    score: int
    players_on_wall: typing.List[typing.Any]
    name: str
    id: FactionId
    chain: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarFaction(
            score=BaseSchema.parse(data.get("score"), int),
            players_on_wall=BaseSchema.parse(
                data.get("players_on_wall"), typing.List[typing.Any]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            chain=BaseSchema.parse(data.get("chain"), int),
        )
