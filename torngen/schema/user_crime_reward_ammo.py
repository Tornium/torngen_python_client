import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeRewardAmmo(BaseSchema):
    """
    JSON object of `UserCrimeRewardAmmo`.
    """

    standard: int
    special: int

    @staticmethod
    def parse(data):
        return UserCrimeRewardAmmo(
            standard=BaseSchema.parse(data.get("standard"), int),
            special=BaseSchema.parse(data.get("special"), int),
        )
