import typing

from PersonalStatsAttackingExtended import PersonalStatsAttackingExtended
from PersonalStatsBattleStats import PersonalStatsBattleStats
from PersonalStatsBounties import PersonalStatsBounties
from PersonalStatsCommunication import PersonalStatsCommunication
from PersonalStatsCrimes import PersonalStatsCrimes
from PersonalStatsDrugs import PersonalStatsDrugs
from PersonalStatsFinishingHits import PersonalStatsFinishingHits
from PersonalStatsHospital import PersonalStatsHospital
from PersonalStatsInvestments import PersonalStatsInvestments
from PersonalStatsItems import PersonalStatsItems
from PersonalStatsJail import PersonalStatsJail
from PersonalStatsJobsExtended import PersonalStatsJobsExtended
from PersonalStatsMissions import PersonalStatsMissions
from PersonalStatsNetworthExtended import PersonalStatsNetworthExtended
from PersonalStatsOther import PersonalStatsOther
from PersonalStatsRacing import PersonalStatsRacing
from PersonalStatsTrading import PersonalStatsTrading
from PersonalStatsTravel import PersonalStatsTravel

from ..base_schema import BaseSchema


class UserPersonalStatsFull(BaseSchema):

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
