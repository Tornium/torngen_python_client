import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime_reward_item import UserCrimeRewardItem
from .user_crime_uniques_reward_ammo import UserCrimeUniquesRewardAmmo
from .user_crime_uniques_reward_money import UserCrimeUniquesRewardMoney


@dataclass
class UserCrimeUniquesReward(BaseSchema):
    """
    JSON object of `UserCrimeUniquesReward`.
    """

    money: None | UserCrimeUniquesRewardMoney
    items: typing.List[UserCrimeRewardItem]
    ammo: None | UserCrimeUniquesRewardAmmo

    @staticmethod
    def parse(data):
        return UserCrimeUniquesReward(
            money=BaseSchema.parse(
                data.get("money"), None | UserCrimeUniquesRewardMoney
            ),
            items=BaseSchema.parse(data.get("items"), typing.List[UserCrimeRewardItem]),
            ammo=BaseSchema.parse(data.get("ammo"), None | UserCrimeUniquesRewardAmmo),
        )
