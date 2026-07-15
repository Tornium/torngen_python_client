import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime


@dataclass
class UserOrganizedCrimesResponse(BaseSchema):
    """
    JSON object of `UserOrganizedCrimesResponse`.
    """

    organizedcrimes: typing.List[FactionCrime]

    @staticmethod
    def parse(data):
        return UserOrganizedCrimesResponse(
            organizedcrimes=BaseSchema.parse(
                data.get("organizedcrimes"), typing.List[FactionCrime]
            ),
        )
