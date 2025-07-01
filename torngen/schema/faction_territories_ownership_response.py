import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_ownership import FactionTerritoryOwnership


@dataclass
class FactionTerritoriesOwnershipResponse(BaseSchema):
    """
    JSON object of `FactionTerritoriesOwnershipResponse`.
    """

    territoryownership: typing.List[FactionTerritoryOwnership]

    @staticmethod
    def parse(data):
        return FactionTerritoriesOwnershipResponse(
            territoryownership=BaseSchema.parse(
                data.get("territoryownership"), typing.List[FactionTerritoryOwnership]
            ),
        )
