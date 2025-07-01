import typing

from FactionId import FactionId
from FactionTerritoryEnum import FactionTerritoryEnum
from FactionTerritoryWarReportFaction import FactionTerritoryWarReportFaction
from TerritoryWarId import TerritoryWarId

from ..base_schema import BaseSchema


class FactionTerritoryWarReport(BaseSchema):

    winner: FactionId
    territory: FactionTerritoryEnum
    started_at: int
    result: str
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarReportFaction]
    ended_at: int
