import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime_uniques_reward_ammo_enum import UserCrimeUniquesRewardAmmoEnum


@dataclass
class UserCrimeUniquesRewardAmmo(BaseSchema):
    """
    JSON object of `UserCrimeUniquesRewardAmmo`.
    """

    type: UserCrimeUniquesRewardAmmoEnum
    amount: int

    @staticmethod
    def parse(data):
        return UserCrimeUniquesRewardAmmo(
            type=BaseSchema.parse(data.get("type"), UserCrimeUniquesRewardAmmoEnum),
            amount=BaseSchema.parse(data.get("amount"), int),
        )
