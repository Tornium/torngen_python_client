import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_territory import TornTerritory


@dataclass
class TornTerritoriesNoLinksReponse(BaseSchema):
    """
    JSON object of `TornTerritoriesNoLinksReponse`.
    """

    territory: typing.List[TornTerritory]

    @staticmethod
    def parse(data):
        return TornTerritoriesNoLinksReponse(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[TornTerritory]
            ),
        )
