import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory import FactionTerritory


@dataclass
class FactionTerritoriesReponse(BaseSchema):
    """
    JSON object of `FactionTerritoriesReponse`.
    """

    territory: typing.List[FactionTerritory]

    @staticmethod
    def parse(data):
        return FactionTerritoriesReponse(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[FactionTerritory]
            ),
        )
