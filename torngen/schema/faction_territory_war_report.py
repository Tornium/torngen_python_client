import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_territory_enum import FactionTerritoryEnum
from .faction_territory_war_report_faction import \
    FactionTerritoryWarReportFaction
from .territory_war_id import TerritoryWarId


@dataclass
class FactionTerritoryWarReport(BaseSchema):
    """
    JSON object of `FactionTerritoryWarReport`.
    """

    winner: FactionId
    territory: FactionTerritoryEnum
    started_at: int
    result: str
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarReportFaction]
    ended_at: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarReport(
            winner=BaseSchema.parse(data.get("winner"), FactionId),
            territory=BaseSchema.parse(data.get("territory"), FactionTerritoryEnum),
            started_at=BaseSchema.parse(data.get("started_at"), int),
            result=BaseSchema.parse(data.get("result"), str),
            id=BaseSchema.parse(data.get("id"), TerritoryWarId),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionTerritoryWarReportFaction]
            ),
            ended_at=BaseSchema.parse(data.get("ended_at"), int),
        )
