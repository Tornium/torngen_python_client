import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_travel_inventory_item import UserTravelInventoryItem


@dataclass
class UserTravelInventorySlot(BaseSchema):
    """
    JSON object of `UserTravelInventorySlot`.
    """

    item: None | UserTravelInventoryItem
    id: int

    @staticmethod
    def parse(data):
        return UserTravelInventorySlot(
            item=BaseSchema.parse(data.get("item"), None | UserTravelInventoryItem),
            id=BaseSchema.parse(data.get("id"), int),
        )
