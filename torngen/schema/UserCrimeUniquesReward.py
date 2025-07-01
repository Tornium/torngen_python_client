import typing

from UserCrimeRewardItem import UserCrimeRewardItem
from UserCrimeUniquesRewardAmmo import UserCrimeUniquesRewardAmmo
from UserCrimeUniquesRewardMoney import UserCrimeUniquesRewardMoney

from ..base_schema import BaseSchema


class UserCrimeUniquesReward(BaseSchema):

    money: None | UserCrimeUniquesRewardMoney
    items: typing.List[UserCrimeRewardItem]
    ammo: None | UserCrimeUniquesRewardAmmo
