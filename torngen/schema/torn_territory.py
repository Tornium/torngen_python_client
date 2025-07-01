import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_enum import FactionTerritoryEnum
from .torn_territory_coordinates import TornTerritoryCoordinates


@dataclass
class TornTerritory(BaseSchema):
    """
    JSON object of `TornTerritory`.
    """

    slots: int
    size: int
    sector: int
    respect: int
    neighbors: typing.List[FactionTerritoryEnum]
    id: FactionTerritoryEnum
    density: int
    coordinates: TornTerritoryCoordinates

    @staticmethod
    def parse(data):
        return TornTerritory(
            slots=BaseSchema.parse(data.get("slots"), int),
            size=BaseSchema.parse(data.get("size"), int),
            sector=BaseSchema.parse(data.get("sector"), int),
            respect=BaseSchema.parse(data.get("respect"), int),
            neighbors=BaseSchema.parse(
                data.get("neighbors"), typing.List[FactionTerritoryEnum]
            ),
            id=BaseSchema.parse(data.get("id"), FactionTerritoryEnum),
            density=BaseSchema.parse(data.get("density"), int),
            coordinates=BaseSchema.parse(
                data.get("coordinates"), TornTerritoryCoordinates
            ),
        )
