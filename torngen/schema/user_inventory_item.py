import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid


@dataclass
class UserInventoryItem(BaseSchema):
    """
    JSON object of `UserInventoryItem`.
    """

    uid: None | ItemUid
    name: str
    id: ItemId
    faction_owned: bool
    equipped: bool
    amount: int

    @staticmethod
    def parse(data):
        return UserInventoryItem(
            uid=BaseSchema.parse(data.get("uid"), None | ItemUid),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
            faction_owned=BaseSchema.parse(data.get("faction_owned"), bool),
            equipped=BaseSchema.parse(data.get("equipped"), bool),
            amount=BaseSchema.parse(data.get("amount"), int),
        )
