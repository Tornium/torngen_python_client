import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_details import TornItemDetails
from .torn_item_details_deprecated import TornItemDetailsDeprecated


@dataclass
class TornItemDetailsResponse(BaseSchema):
    """
    JSON object of `TornItemDetailsResponse`.
    """

    itemdetails: TornItemDetailsDeprecated | typing.List[TornItemDetails]

    @staticmethod
    def parse(data):
        return TornItemDetailsResponse(
            itemdetails=BaseSchema.parse(
                data.get("itemdetails"),
                TornItemDetailsDeprecated | typing.List[TornItemDetails],
            ),
        )
