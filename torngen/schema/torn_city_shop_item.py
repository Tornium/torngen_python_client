import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class TornCityShopItem(BaseSchema):
    """
    JSON object of `TornCityShopItem`.
    """

    stock: typing.TypedDict("", {"default": int, "current": int})
    price: int
    name: str
    id: ItemId

    @staticmethod
    def parse(data):
        return TornCityShopItem(
            stock=BaseSchema.parse(
                data.get("stock"),
                typing.TypedDict("", {"default": int, "current": int}),
            ),
            price=BaseSchema.parse(data.get("price"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )
