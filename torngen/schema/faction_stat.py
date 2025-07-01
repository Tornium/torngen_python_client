import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_stat_enum import FactionStatEnum


@dataclass
class FactionStat(BaseSchema):
    """
    JSON object of `FactionStat`.
    """

    value: int
    name: FactionStatEnum

    @staticmethod
    def parse(data):
        return FactionStat(
            value=BaseSchema.parse(data.get("value"), int),
            name=BaseSchema.parse(data.get("name"), FactionStatEnum),
        )
