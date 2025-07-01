import typing

from PersonalStatsHistoricStat import PersonalStatsHistoricStat

from ..base_schema import BaseSchema


class UserPersonalStatsHistoric(BaseSchema):

    personalstats: typing.List[PersonalStatsHistoricStat]
