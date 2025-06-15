import typing

from UserCrimeAttempts import UserCrimeAttempts
from UserCrimeDetailsBootlegging import UserCrimeDetailsBootlegging
from UserCrimeDetailsCardSkimming import UserCrimeDetailsCardSkimming
from UserCrimeDetailsCracking import UserCrimeDetailsCracking
from UserCrimeDetailsGraffiti import UserCrimeDetailsGraffiti
from UserCrimeDetailsHustling import UserCrimeDetailsHustling
from UserCrimeDetailsScamming import UserCrimeDetailsScamming
from UserCrimeDetailsShoplifting import UserCrimeDetailsShoplifting
from UserCrimeRewards import UserCrimeRewards
from UserCrimeUniques import UserCrimeUniques

from ..base_schema import BaseSchema


class UserCrime(BaseSchema):

    uniques: typing.List[UserCrimeUniques]
    skill: int
    rewards: UserCrimeRewards
    progression_bonus: int
    nerve_spent: int
    miscellaneous: (
        None
        | UserCrimeDetailsScamming
        | UserCrimeDetailsCracking
        | UserCrimeDetailsHustling
        | UserCrimeDetailsCardSkimming
        | UserCrimeDetailsShoplifting
        | UserCrimeDetailsGraffiti
        | UserCrimeDetailsBootlegging
    )
    attempts: UserCrimeAttempts
