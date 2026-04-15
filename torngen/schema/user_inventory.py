import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_inventory_item import UserInventoryItem


@dataclass
class UserInventory(BaseSchema):
    """
    JSON object of `UserInventory`.
    """

    timestamp: int
    items: typing.List[UserInventoryItem]

    @staticmethod
    def parse(data):
        return UserInventory(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            items=BaseSchema.parse(data.get("items"), typing.List[UserInventoryItem]),
        )
