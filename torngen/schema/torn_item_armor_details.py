import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_armor_coverage import TornItemArmorCoverage
from .torn_item_base_stats import TornItemBaseStats


@dataclass
class TornItemArmorDetails(BaseSchema):
    """
    JSON object of `TornItemArmorDetails`.
    """

    coverage: typing.List[TornItemArmorCoverage]
    base_stats: TornItemBaseStats

    @staticmethod
    def parse(data):
        return TornItemArmorDetails(
            coverage=BaseSchema.parse(
                data.get("coverage"), typing.List[TornItemArmorCoverage]
            ),
            base_stats=BaseSchema.parse(data.get("base_stats"), TornItemBaseStats),
        )
