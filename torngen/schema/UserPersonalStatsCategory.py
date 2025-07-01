import typing

from PersonalStatsAttackingPublic import PersonalStatsAttackingPublic
from PersonalStatsBounties import PersonalStatsBounties
from PersonalStatsCommunication import PersonalStatsCommunication
from PersonalStatsCrimes import PersonalStatsCrimes
from PersonalStatsDrugs import PersonalStatsDrugs
from PersonalStatsFinishingHits import PersonalStatsFinishingHits
from PersonalStatsHospital import PersonalStatsHospital
from PersonalStatsItems import PersonalStatsItems
from PersonalStatsJail import PersonalStatsJail
from PersonalStatsJobsPublic import PersonalStatsJobsPublic
from PersonalStatsMissions import PersonalStatsMissions
from PersonalStatsNetworthPublic import PersonalStatsNetworthPublic
from PersonalStatsOther import PersonalStatsOther
from PersonalStatsRacing import PersonalStatsRacing
from PersonalStatsTrading import PersonalStatsTrading
from PersonalStatsTravel import PersonalStatsTravel

from ..base_schema import BaseSchema


class UserPersonalStatsCategory(BaseSchema):

    personalstats: (
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
    )
