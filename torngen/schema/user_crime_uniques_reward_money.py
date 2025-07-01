import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeUniquesRewardMoney(BaseSchema):
    """
    JSON object of `UserCrimeUniquesRewardMoney`.
    """

    min: int
    max: int

    @staticmethod
    def parse(data):
        return UserCrimeUniquesRewardMoney(
            min=BaseSchema.parse(data.get("min"), int),
            max=BaseSchema.parse(data.get("max"), int),
        )
