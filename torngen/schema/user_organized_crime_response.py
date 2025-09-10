import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime import FactionCrime
from .user_organized_crime_error import UserOrganizedCrimeError


@dataclass
class UserOrganizedCrimeResponse(BaseSchema):
    """
    JSON object of `UserOrganizedCrimeResponse`.
    """

    organizedCrime: None | UserOrganizedCrimeError | FactionCrime

    @staticmethod
    def parse(data):
        return UserOrganizedCrimeResponse(
            organizedCrime=BaseSchema.parse(
                data.get("organizedCrime"),
                None | UserOrganizedCrimeError | FactionCrime,
            ),
        )
