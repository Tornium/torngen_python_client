import typing

from FactionTerritoryEnum import FactionTerritoryEnum
from TornRacket import TornRacket
from TornTerritoryCoordinates import TornTerritoryCoordinates

from ..base_schema import BaseSchema


class FactionTerritory(BaseSchema):

    slots: int
    size: int
    sector: int
    respect: int
    racket: None | TornRacket
    id: FactionTerritoryEnum
    density: int
    coordinates: TornTerritoryCoordinates
    acquired_at: int
