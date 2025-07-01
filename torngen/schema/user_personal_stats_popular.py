import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_attacking_popular import PersonalStatsAttackingPopular
from .personal_stats_crimes_popular import PersonalStatsCrimesPopular
from .personal_stats_drugs import PersonalStatsDrugs
from .personal_stats_hospital_popular import PersonalStatsHospitalPopular
from .personal_stats_items_popular import PersonalStatsItemsPopular
from .personal_stats_jobs_public import PersonalStatsJobsPublic
from .personal_stats_networth_public import PersonalStatsNetworthPublic
from .personal_stats_other_popular import PersonalStatsOtherPopular
from .personal_stats_travel_popular import PersonalStatsTravelPopular


@dataclass
class UserPersonalStatsPopular(BaseSchema):
    """
    JSON object of `UserPersonalStatsPopular`.
    """

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

    @staticmethod
    def parse(data):
        return UserPersonalStatsPopular(
            personalstats=BaseSchema.parse(
                data.get("personalstats"),
                typing.List[
                    PersonalStatsOtherPopular
                    | PersonalStatsNetworthPublic
                    | PersonalStatsDrugs
                    | PersonalStatsTravelPopular
                    | PersonalStatsItemsPopular
                    | PersonalStatsCrimesPopular
                    | PersonalStatsHospitalPopular
                    | PersonalStatsJobsPublic
                    | PersonalStatsAttackingPopular
                ],
            ),
        )
