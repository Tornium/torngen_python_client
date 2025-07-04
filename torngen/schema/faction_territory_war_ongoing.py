import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_enum import FactionTerritoryEnum
from .faction_territory_war_ongoing_faction import FactionTerritoryWarOngoingFaction
from .territory_war_id import TerritoryWarId


@dataclass
class FactionTerritoryWarOngoing(BaseSchema):
    """
    JSON object of `FactionTerritoryWarOngoing`.
    """

    territory: FactionTerritoryEnum
    target: int
    start: int
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarOngoingFaction]
    end: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarOngoing(
            territory=BaseSchema.parse(data.get("territory"), FactionTerritoryEnum),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            id=BaseSchema.parse(data.get("id"), TerritoryWarId),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionTerritoryWarOngoingFaction]
            ),
            end=BaseSchema.parse(data.get("end"), int),
        )
