import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class FactionOcHistoryItem(BaseSchema):
    """
    JSON object of `FactionOcHistoryItem`.
    """

    quantity: int
    item_name: str
    item_id: ItemId

    @staticmethod
    def parse(data):
        return FactionOcHistoryItem(
            quantity=BaseSchema.parse(data.get("quantity"), int),
            item_name=BaseSchema.parse(data.get("item_name"), str),
            item_id=BaseSchema.parse(data.get("item_id"), ItemId),
        )
