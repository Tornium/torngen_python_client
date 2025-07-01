import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_historic_stat import PersonalStatsHistoricStat


@dataclass
class UserPersonalStatsHistoric(BaseSchema):
    """
    JSON object of `UserPersonalStatsHistoric`.
    """

    personalstats: typing.List[PersonalStatsHistoricStat]

    @staticmethod
    def parse(data):
        return UserPersonalStatsHistoric(
            personalstats=BaseSchema.parse(
                data.get("personalstats"), typing.List[PersonalStatsHistoricStat]
            ),
        )
