import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_armor_coverage_part_enum import TornItemArmorCoveragePartEnum


@dataclass
class TornItemArmorCoverage(BaseSchema):
    """
    JSON object of `TornItemArmorCoverage`.
    """

    value: int | float
    name: TornItemArmorCoveragePartEnum

    @staticmethod
    def parse(data):
        return TornItemArmorCoverage(
            value=BaseSchema.parse(data.get("value"), int | float),
            name=BaseSchema.parse(data.get("name"), TornItemArmorCoveragePartEnum),
        )
