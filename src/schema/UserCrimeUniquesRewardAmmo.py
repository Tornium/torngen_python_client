import typing

from UserCrimeUniquesRewardAmmoEnum import UserCrimeUniquesRewardAmmoEnum

from ..base_schema import BaseSchema


class UserCrimeUniquesRewardAmmo(BaseSchema):

    type: UserCrimeUniquesRewardAmmoEnum
    amount: int
