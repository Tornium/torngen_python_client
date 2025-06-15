import typing

from FactionTerritoryEnum import FactionTerritoryEnum
from FactionTerritoryWarFaction import FactionTerritoryWarFaction
from TerritoryWarId import TerritoryWarId

from ..base_schema import BaseSchema


class FactionTerritoryWarfare(BaseSchema):

    territory: FactionTerritoryEnum
    target: int
    start: int
    result: str
    id: TerritoryWarId
    end: int
    defender: FactionTerritoryWarFaction
    aggressor: FactionTerritoryWarFaction
