import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_enum import FactionTerritoryEnum
from .torn_racket import TornRacket
from .torn_territory_coordinates import TornTerritoryCoordinates


@dataclass
class FactionTerritory(BaseSchema):
    """
    JSON object of `FactionTerritory`.
    """

    slots: int
    size: int
    sector: int
    respect: int
    racket: None | TornRacket
    id: FactionTerritoryEnum
    density: int
    coordinates: TornTerritoryCoordinates
    acquired_at: int

    @staticmethod
    def parse(data):
        return FactionTerritory(
            slots=BaseSchema.parse(data.get("slots"), int),
            size=BaseSchema.parse(data.get("size"), int),
            sector=BaseSchema.parse(data.get("sector"), int),
            respect=BaseSchema.parse(data.get("respect"), int),
            racket=BaseSchema.parse(data.get("racket"), None | TornRacket),
            id=BaseSchema.parse(data.get("id"), FactionTerritoryEnum),
            density=BaseSchema.parse(data.get("density"), int),
            coordinates=BaseSchema.parse(
                data.get("coordinates"), TornTerritoryCoordinates
            ),
            acquired_at=BaseSchema.parse(data.get("acquired_at"), int),
        )
