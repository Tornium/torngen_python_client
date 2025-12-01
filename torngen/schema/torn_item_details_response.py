import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_details import TornItemDetails


@dataclass
class TornItemDetailsResponse(BaseSchema):
    """
    JSON object of `TornItemDetailsResponse`.
    """

    itemdetails: TornItemDetails

    @staticmethod
    def parse(data):
        return TornItemDetailsResponse(
            itemdetails=BaseSchema.parse(data.get("itemdetails"), TornItemDetails),
        )
