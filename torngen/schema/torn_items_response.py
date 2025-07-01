import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item import TornItem


@dataclass
class TornItemsResponse(BaseSchema):
    """
    JSON object of `TornItemsResponse`.
    """

    items: typing.List[TornItem]

    @staticmethod
    def parse(data):
        return TornItemsResponse(
            items=BaseSchema.parse(data.get("items"), typing.List[TornItem]),
        )
