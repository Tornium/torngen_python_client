import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_stats import TornItemStats


@dataclass
class TornItemStatsResponse(BaseSchema):
    """
    JSON object of `TornItemStatsResponse`.
    """

    itemdetails: typing.List[TornItemStats]

    @staticmethod
    def parse(data):
        return TornItemStatsResponse(
            itemdetails=BaseSchema.parse(
                data.get("itemdetails"), typing.List[TornItemStats]
            ),
        )
