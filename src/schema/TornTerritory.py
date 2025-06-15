import typing

from FactionTerritoryEnum import FactionTerritoryEnum
from TornTerritoryCoordinates import TornTerritoryCoordinates

from ..base_schema import BaseSchema


class TornTerritory(BaseSchema):

    slots: int
    size: int
    sector: int
    respect: int
    neighbors: typing.List[FactionTerritoryEnum]
    id: FactionTerritoryEnum
    density: int
    coordinates: TornTerritoryCoordinates
