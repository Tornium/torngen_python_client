import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_organized_crime import TornOrganizedCrime


@dataclass
class TornOrganizedCrimeResponse(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeResponse`.
    """

    organizedcrimes: typing.List[TornOrganizedCrime]

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeResponse(
            organizedcrimes=BaseSchema.parse(
                data.get("organizedcrimes"), typing.List[TornOrganizedCrime]
            ),
        )
