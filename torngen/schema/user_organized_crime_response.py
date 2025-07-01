import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime


@dataclass
class UserOrganizedCrimeResponse(BaseSchema):
    """
    JSON object of `UserOrganizedCrimeResponse`.
    """

    organizedCrime: None | FactionCrime

    @staticmethod
    def parse(data):
        return UserOrganizedCrimeResponse(
            organizedCrime=BaseSchema.parse(
                data.get("organizedCrime"), None | FactionCrime
            ),
        )
