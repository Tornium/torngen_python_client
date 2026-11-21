import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid
from .torn_inventory_item_type import TornInventoryItemType
from .user_armoury_item_details import UserArmouryItemDetails


@dataclass
class UserDisplayItem(BaseSchema):
    """
    JSON object of `UserDisplayItem`.
    """

    uids: typing.List[ItemUid]
    type: TornInventoryItemType
    quantity: int
    name: str
    market_price: int
    item_details: None | UserArmouryItemDetails
    id: ItemId
    circulation: int

    @staticmethod
    def parse(data):
        return UserDisplayItem(
            uids=BaseSchema.parse(data.get("uids"), typing.List[ItemUid]),
            type=BaseSchema.parse(data.get("type"), TornInventoryItemType),
            quantity=BaseSchema.parse(data.get("quantity"), int),
            name=BaseSchema.parse(data.get("name"), str),
            market_price=BaseSchema.parse(data.get("market_price"), int),
            item_details=BaseSchema.parse(
                data.get("item_details"), None | UserArmouryItemDetails
            ),
            id=BaseSchema.parse(data.get("id"), ItemId),
            circulation=BaseSchema.parse(data.get("circulation"), int),
        )
