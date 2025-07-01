import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime


@dataclass
class FactionCrimeResponse(BaseSchema):
    """
    JSON object of `FactionCrimeResponse`.
    """

    crime: FactionCrime

    @staticmethod
    def parse(data):
        return FactionCrimeResponse(
            crime=BaseSchema.parse(data.get("crime"), FactionCrime),
        )
