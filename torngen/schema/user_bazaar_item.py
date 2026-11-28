import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .torn_inventory_item_type import TornInventoryItemType
from .user_armoury_item_details import UserArmouryItemDetails
from .user_bazaar_item_uid import UserBazaarItemUid


@dataclass
class UserBazaarItem(BaseSchema):
    """
    JSON object of `UserBazaarItem`.
    """

    uids: typing.List[UserBazaarItemUid]
    type: TornInventoryItemType
    quantity: int
    price: None | int
    name: str
    market_price: int
    item_details: None | UserArmouryItemDetails
    id: ItemId

    @staticmethod
    def parse(data):
        return UserBazaarItem(
            uids=BaseSchema.parse(data.get("uids"), typing.List[UserBazaarItemUid]),
            type=BaseSchema.parse(data.get("type"), TornInventoryItemType),
            quantity=BaseSchema.parse(data.get("quantity"), int),
            price=BaseSchema.parse(data.get("price"), None | int),
            name=BaseSchema.parse(data.get("name"), str),
            market_price=BaseSchema.parse(data.get("market_price"), int),
            item_details=BaseSchema.parse(
                data.get("item_details"), None | UserArmouryItemDetails
            ),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )
