import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_hof_stats import FactionHofStats


@dataclass
class FactionHofResponse(BaseSchema):
    """
    JSON object of `FactionHofResponse`.
    """

    hof: FactionHofStats

    @staticmethod
    def parse(data):
        return FactionHofResponse(
            hof=BaseSchema.parse(data.get("hof"), FactionHofStats),
        )
