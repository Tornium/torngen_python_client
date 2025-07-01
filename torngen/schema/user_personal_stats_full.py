import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_attacking_extended import PersonalStatsAttackingExtended
from .personal_stats_battle_stats import PersonalStatsBattleStats
from .personal_stats_bounties import PersonalStatsBounties
from .personal_stats_communication import PersonalStatsCommunication
from .personal_stats_crimes import PersonalStatsCrimes
from .personal_stats_drugs import PersonalStatsDrugs
from .personal_stats_finishing_hits import PersonalStatsFinishingHits
from .personal_stats_hospital import PersonalStatsHospital
from .personal_stats_investments import PersonalStatsInvestments
from .personal_stats_items import PersonalStatsItems
from .personal_stats_jail import PersonalStatsJail
from .personal_stats_jobs_extended import PersonalStatsJobsExtended
from .personal_stats_missions import PersonalStatsMissions
from .personal_stats_networth_extended import PersonalStatsNetworthExtended
from .personal_stats_other import PersonalStatsOther
from .personal_stats_racing import PersonalStatsRacing
from .personal_stats_trading import PersonalStatsTrading
from .personal_stats_travel import PersonalStatsTravel


@dataclass
class UserPersonalStatsFull(BaseSchema):
    """
    JSON object of `UserPersonalStatsFull`.
    """

    personalstats: typing.List[
        PersonalStatsOther
        | PersonalStatsNetworthExtended
        | PersonalStatsRacing
        | PersonalStatsMissions
        | PersonalStatsDrugs
        | PersonalStatsTravel
        | PersonalStatsItems
        | PersonalStatsInvestments
        | PersonalStatsBounties
        | PersonalStatsCrimes
        | PersonalStatsCommunication
        | PersonalStatsFinishingHits
        | PersonalStatsHospital
        | PersonalStatsJail
        | PersonalStatsTrading
        | PersonalStatsJobsExtended
        | PersonalStatsBattleStats
        | PersonalStatsAttackingExtended
    ]

    @staticmethod
    def parse(data):
        return UserPersonalStatsFull(
            personalstats=BaseSchema.parse(
                data.get("personalstats"),
                typing.List[
                    PersonalStatsOther
                    | PersonalStatsNetworthExtended
                    | PersonalStatsRacing
                    | PersonalStatsMissions
                    | PersonalStatsDrugs
                    | PersonalStatsTravel
                    | PersonalStatsItems
                    | PersonalStatsInvestments
                    | PersonalStatsBounties
                    | PersonalStatsCrimes
                    | PersonalStatsCommunication
                    | PersonalStatsFinishingHits
                    | PersonalStatsHospital
                    | PersonalStatsJail
                    | PersonalStatsTrading
                    | PersonalStatsJobsExtended
                    | PersonalStatsBattleStats
                    | PersonalStatsAttackingExtended
                ],
            ),
        )
