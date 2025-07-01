import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime_attempts import UserCrimeAttempts
from .user_crime_details_bootlegging import UserCrimeDetailsBootlegging
from .user_crime_details_card_skimming import UserCrimeDetailsCardSkimming
from .user_crime_details_cracking import UserCrimeDetailsCracking
from .user_crime_details_graffiti import UserCrimeDetailsGraffiti
from .user_crime_details_hustling import UserCrimeDetailsHustling
from .user_crime_details_scamming import UserCrimeDetailsScamming
from .user_crime_details_shoplifting import UserCrimeDetailsShoplifting
from .user_crime_rewards import UserCrimeRewards
from .user_crime_uniques import UserCrimeUniques


@dataclass
class UserCrime(BaseSchema):
    """
    JSON object of `UserCrime`.
    """

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

    @staticmethod
    def parse(data):
        return UserCrime(
            uniques=BaseSchema.parse(
                data.get("uniques"), typing.List[UserCrimeUniques]
            ),
            skill=BaseSchema.parse(data.get("skill"), int),
            rewards=BaseSchema.parse(data.get("rewards"), UserCrimeRewards),
            progression_bonus=BaseSchema.parse(data.get("progression_bonus"), int),
            nerve_spent=BaseSchema.parse(data.get("nerve_spent"), int),
            miscellaneous=BaseSchema.parse(
                data.get("miscellaneous"),
                None
                | UserCrimeDetailsScamming
                | UserCrimeDetailsCracking
                | UserCrimeDetailsHustling
                | UserCrimeDetailsCardSkimming
                | UserCrimeDetailsShoplifting
                | UserCrimeDetailsGraffiti
                | UserCrimeDetailsBootlegging,
            ),
            attempts=BaseSchema.parse(data.get("attempts"), UserCrimeAttempts),
        )
