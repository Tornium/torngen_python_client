import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_crime import TornCrime


@dataclass
class TornCrimesResponse(BaseSchema):
    """
    JSON object of `TornCrimesResponse`.
    """

    crimes: typing.List[TornCrime]

    @staticmethod
    def parse(data):
        return TornCrimesResponse(
            crimes=BaseSchema.parse(data.get("crimes"), typing.List[TornCrime]),
        )
