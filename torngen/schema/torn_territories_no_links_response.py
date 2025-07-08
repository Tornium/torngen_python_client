import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_territory import TornTerritory


@dataclass
class TornTerritoriesNoLinksResponse(BaseSchema):
    """
    JSON object of `TornTerritoriesNoLinksResponse`.
    """

    territory: typing.List[TornTerritory]

    @staticmethod
    def parse(data):
        return TornTerritoriesNoLinksResponse(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[TornTerritory]
            ),
        )
