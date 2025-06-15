import typing

from ..base_schema import BaseSchema


class PersonalStatsHistoricStat(BaseSchema):

    value: int
    timestamp: int
    name: str
