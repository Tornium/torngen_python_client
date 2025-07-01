import typing

from FactionTerritoryEnum import FactionTerritoryEnum
from FactionTerritoryWarFinishedFaction import \
    FactionTerritoryWarFinishedFaction
from FactionTerritoryWarResultEnum import FactionTerritoryWarResultEnum
from TerritoryWarId import TerritoryWarId

from ..base_schema import BaseSchema


class FactionTerritoryWarFinished(BaseSchema):

    territory: FactionTerritoryEnum
    target: int
    start: int
    result: FactionTerritoryWarResultEnum
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarFinishedFaction]
    end: int
