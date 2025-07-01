import typing

from FactionTerritoryEnum import FactionTerritoryEnum
from FactionTerritoryWarOngoingFaction import FactionTerritoryWarOngoingFaction
from TerritoryWarId import TerritoryWarId

from ..base_schema import BaseSchema


class FactionTerritoryWarOngoing(BaseSchema):

    territory: FactionTerritoryEnum
    target: int
    start: int
    id: TerritoryWarId
    factions: typing.List[FactionTerritoryWarOngoingFaction]
    end: int
