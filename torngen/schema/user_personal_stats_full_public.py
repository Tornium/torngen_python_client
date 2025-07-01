import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_attacking_public import PersonalStatsAttackingPublic
from .personal_stats_bounties import PersonalStatsBounties
from .personal_stats_communication import PersonalStatsCommunication
from .personal_stats_crimes import PersonalStatsCrimes
from .personal_stats_drugs import PersonalStatsDrugs
from .personal_stats_finishing_hits import PersonalStatsFinishingHits
from .personal_stats_hospital import PersonalStatsHospital
from .personal_stats_items import PersonalStatsItems
from .personal_stats_jail import PersonalStatsJail
from .personal_stats_jobs_public import PersonalStatsJobsPublic
from .personal_stats_missions import PersonalStatsMissions
from .personal_stats_networth_public import PersonalStatsNetworthPublic
from .personal_stats_other import PersonalStatsOther
from .personal_stats_racing import PersonalStatsRacing
from .personal_stats_trading import PersonalStatsTrading
from .personal_stats_travel import PersonalStatsTravel


@dataclass
class UserPersonalStatsFullPublic(BaseSchema):
    """
    JSON object of `UserPersonalStatsFullPublic`.
    """

    personalstats: typing.List[
        PersonalStatsOther
        | PersonalStatsNetworthPublic
        | PersonalStatsRacing
        | PersonalStatsMissions
        | PersonalStatsDrugs
        | PersonalStatsTravel
        | PersonalStatsItems
        | PersonalStatsBounties
        | PersonalStatsCrimes
        | PersonalStatsCommunication
        | PersonalStatsFinishingHits
        | PersonalStatsHospital
        | PersonalStatsJail
        | PersonalStatsTrading
        | PersonalStatsJobsPublic
        | PersonalStatsAttackingPublic
    ]

    @staticmethod
    def parse(data):
        return UserPersonalStatsFullPublic(
            personalstats=BaseSchema.parse(
                data.get("personalstats"),
                typing.List[
                    PersonalStatsOther
                    | PersonalStatsNetworthPublic
                    | PersonalStatsRacing
                    | PersonalStatsMissions
                    | PersonalStatsDrugs
                    | PersonalStatsTravel
                    | PersonalStatsItems
                    | PersonalStatsBounties
                    | PersonalStatsCrimes
                    | PersonalStatsCommunication
                    | PersonalStatsFinishingHits
                    | PersonalStatsHospital
                    | PersonalStatsJail
                    | PersonalStatsTrading
                    | PersonalStatsJobsPublic
                    | PersonalStatsAttackingPublic
                ],
            ),
        )
