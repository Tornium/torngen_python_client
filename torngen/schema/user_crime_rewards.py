import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime_reward_ammo import UserCrimeRewardAmmo
from .user_crime_reward_item import UserCrimeRewardItem


@dataclass
class UserCrimeRewards(BaseSchema):
    """
    JSON object of `UserCrimeRewards`.
    """

    money: int
    items: typing.List[UserCrimeRewardItem]
    ammo: UserCrimeRewardAmmo

    @staticmethod
    def parse(data):
        return UserCrimeRewards(
            money=BaseSchema.parse(data.get("money"), int),
            items=BaseSchema.parse(data.get("items"), typing.List[UserCrimeRewardItem]),
            ammo=BaseSchema.parse(data.get("ammo"), UserCrimeRewardAmmo),
        )
