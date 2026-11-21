import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid


@dataclass
class UserTravelInventoryItem(BaseSchema):
    """
    JSON object of `UserTravelInventoryItem`.
    """

    uid: None | ItemUid
    type: str
    name: str
    is_permanent: bool
    is_faction_owned: bool
    is_equipped: bool
    id: ItemId

    @staticmethod
    def parse(data):
        return UserTravelInventoryItem(
            uid=BaseSchema.parse(data.get("uid"), None | ItemUid),
            type=BaseSchema.parse(data.get("type"), str),
            name=BaseSchema.parse(data.get("name"), str),
            is_permanent=BaseSchema.parse(data.get("is_permanent"), bool),
            is_faction_owned=BaseSchema.parse(data.get("is_faction_owned"), bool),
            is_equipped=BaseSchema.parse(data.get("is_equipped"), bool),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )
