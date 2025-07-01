import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class ItemMarketItem(BaseSchema):
    """
    JSON object of `ItemMarketItem`.
    """

    type: str
    name: str
    id: ItemId
    average_price: int

    @staticmethod
    def parse(data):
        return ItemMarketItem(
            type=BaseSchema.parse(data.get("type"), str),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
            average_price=BaseSchema.parse(data.get("average_price"), int),
        )
