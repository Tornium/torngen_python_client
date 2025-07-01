import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_enum import FactionTerritoryEnum
from .faction_territory_war_faction import FactionTerritoryWarFaction
from .territory_war_id import TerritoryWarId


@dataclass
class FactionTerritoryWarfare(BaseSchema):
    """
    JSON object of `FactionTerritoryWarfare`.
    """

    territory: FactionTerritoryEnum
    target: int
    start: int
    result: str
    id: TerritoryWarId
    end: int
    defender: FactionTerritoryWarFaction
    aggressor: FactionTerritoryWarFaction

    @staticmethod
    def parse(data):
        return FactionTerritoryWarfare(
            territory=BaseSchema.parse(data.get("territory"), FactionTerritoryEnum),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            result=BaseSchema.parse(data.get("result"), str),
            id=BaseSchema.parse(data.get("id"), TerritoryWarId),
            end=BaseSchema.parse(data.get("end"), int),
            defender=BaseSchema.parse(data.get("defender"), FactionTerritoryWarFaction),
            aggressor=BaseSchema.parse(
                data.get("aggressor"), FactionTerritoryWarFaction
            ),
        )
