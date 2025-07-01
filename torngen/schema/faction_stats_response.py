import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_stat import FactionStat


@dataclass
class FactionStatsResponse(BaseSchema):
    """
    JSON object of `FactionStatsResponse`.
    """

    stats: typing.List[FactionStat]

    @staticmethod
    def parse(data):
        return FactionStatsResponse(
            stats=BaseSchema.parse(data.get("stats"), typing.List[FactionStat]),
        )
