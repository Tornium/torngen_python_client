import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsHistoricStat(BaseSchema):
    """
    JSON object of `PersonalStatsHistoricStat`.
    """

    value: int
    timestamp: int
    name: str

    @staticmethod
    def parse(data):
        return PersonalStatsHistoricStat(
            value=BaseSchema.parse(data.get("value"), int),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            name=BaseSchema.parse(data.get("name"), str),
        )
