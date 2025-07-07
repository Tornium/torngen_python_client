import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_ownership import FactionTerritoryOwnership


@dataclass
class FactionTerritoriesOwnershipResponse(BaseSchema):
    """
    JSON object of `FactionTerritoriesOwnershipResponse`.
    """

    territoryOwnership: typing.List[FactionTerritoryOwnership]

    @staticmethod
    def parse(data):
        return FactionTerritoriesOwnershipResponse(
            territoryOwnership=BaseSchema.parse(
                data.get("territoryOwnership"), typing.List[FactionTerritoryOwnership]
            ),
        )
