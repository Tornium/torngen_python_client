import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_enum import FactionTerritoryEnum
from .faction_territory_war_finished_faction import FactionTerritoryWarFinishedFaction
from .faction_territory_war_result_enum import FactionTerritoryWarResultEnum
from .territory_war_id import TerritoryWarId


@dataclass
class FactionTerritoryWarFinished(BaseSchema):
    """
    JSON object of `FactionTerritoryWarFinished`.
    """

    territory: FactionTerritoryEnum
    target: int
    start: int
    result: FactionTerritoryWarResultEnum
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarFinishedFaction]
    end: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarFinished(
            territory=BaseSchema.parse(data.get("territory"), FactionTerritoryEnum),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            result=BaseSchema.parse(data.get("result"), FactionTerritoryWarResultEnum),
            id=BaseSchema.parse(data.get("id"), TerritoryWarId),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionTerritoryWarFinishedFaction]
            ),
            end=BaseSchema.parse(data.get("end"), int),
        )
