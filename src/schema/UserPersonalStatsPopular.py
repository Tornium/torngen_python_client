import typing

from PersonalStatsAttackingPopular import PersonalStatsAttackingPopular
from PersonalStatsCrimesPopular import PersonalStatsCrimesPopular
from PersonalStatsDrugs import PersonalStatsDrugs
from PersonalStatsHospitalPopular import PersonalStatsHospitalPopular
from PersonalStatsItemsPopular import PersonalStatsItemsPopular
from PersonalStatsJobsPublic import PersonalStatsJobsPublic
from PersonalStatsNetworthPublic import PersonalStatsNetworthPublic
from PersonalStatsOtherPopular import PersonalStatsOtherPopular
from PersonalStatsTravelPopular import PersonalStatsTravelPopular

from ..base_schema import BaseSchema


class UserPersonalStatsPopular(BaseSchema):

    personalstats: typing.List[
        PersonalStatsOtherPopular
        | PersonalStatsNetworthPublic
        | PersonalStatsDrugs
        | PersonalStatsTravelPopular
        | PersonalStatsItemsPopular
        | PersonalStatsCrimesPopular
        | PersonalStatsHospitalPopular
        | PersonalStatsJobsPublic
        | PersonalStatsAttackingPopular
    ]
