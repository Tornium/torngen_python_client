import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_travel_inventory_capacity import UserTravelInventoryCapacity
from .user_travel_inventory_slot import UserTravelInventorySlot


@dataclass
class UserTravelInventory(BaseSchema):
    """
    JSON object of `UserTravelInventory`.
    """

    inventory: typing.List[UserTravelInventorySlot]
    capacity: UserTravelInventoryCapacity

    @staticmethod
    def parse(data):
        return UserTravelInventory(
            inventory=BaseSchema.parse(
                data.get("inventory"), typing.List[UserTravelInventorySlot]
            ),
            capacity=BaseSchema.parse(
                data.get("capacity"), UserTravelInventoryCapacity
            ),
        )
