import typing

from UserCrimeUniquesReward import UserCrimeUniquesReward

from ..base_schema import BaseSchema


class UserCrimeUniques(BaseSchema):

    rewards: UserCrimeUniquesReward
    id: int
