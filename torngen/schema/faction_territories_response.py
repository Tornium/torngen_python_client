import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory import FactionTerritory


@dataclass
class FactionTerritoriesResponse(BaseSchema):
    """
    JSON object of `FactionTerritoriesResponse`.
    """

    territory: typing.List[FactionTerritory]

    @staticmethod
    def parse(data):
        return FactionTerritoriesResponse(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[FactionTerritory]
            ),
        )
