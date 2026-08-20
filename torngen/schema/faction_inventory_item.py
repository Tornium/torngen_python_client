import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid
from .market_specialized_bazaar_category_enum import MarketSpecializedBazaarCategoryEnum
from .user_id import UserId


@dataclass
class FactionInventoryItem(BaseSchema):
    """
    JSON object of `FactionInventoryItem`.
    """

    uids: typing.List[ItemUid]
    type: MarketSpecializedBazaarCategoryEnum
    name: str
    loaned: None | typing.TypedDict("", {"name": str, "id": UserId})
    id: ItemId
    amount: int

    @staticmethod
    def parse(data):
        return FactionInventoryItem(
            uids=BaseSchema.parse(data.get("uids"), typing.List[ItemUid]),
            type=BaseSchema.parse(
                data.get("type"), MarketSpecializedBazaarCategoryEnum
            ),
            name=BaseSchema.parse(data.get("name"), str),
            loaned=BaseSchema.parse(
                data.get("loaned"),
                None | typing.TypedDict("", {"name": str, "id": UserId}),
            ),
            id=BaseSchema.parse(data.get("id"), ItemId),
            amount=BaseSchema.parse(data.get("amount"), int),
        )
