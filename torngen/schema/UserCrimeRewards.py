import typing

from UserCrimeRewardAmmo import UserCrimeRewardAmmo
from UserCrimeRewardItem import UserCrimeRewardItem

from ..base_schema import BaseSchema


class UserCrimeRewards(BaseSchema):

    money: int
    items: typing.List[UserCrimeRewardItem]
    ammo: UserCrimeRewardAmmo
