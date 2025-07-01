import typing

from FactionTerritoryOwnership import FactionTerritoryOwnership

from ..base_schema import BaseSchema


class FactionTerritoriesOwnershipResponse(BaseSchema):

    territoryownership: typing.List[FactionTerritoryOwnership]
