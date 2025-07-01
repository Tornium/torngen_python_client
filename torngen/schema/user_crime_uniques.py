import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime_uniques_reward import UserCrimeUniquesReward


@dataclass
class UserCrimeUniques(BaseSchema):
    """
    JSON object of `UserCrimeUniques`.
    """

    rewards: UserCrimeUniquesReward
    id: int

    @staticmethod
    def parse(data):
        return UserCrimeUniques(
            rewards=BaseSchema.parse(data.get("rewards"), UserCrimeUniquesReward),
            id=BaseSchema.parse(data.get("id"), int),
        )
