import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_travel_inventory import UserTravelInventory


@dataclass
class UserTravelInventoryResponse(BaseSchema):
    """
    JSON object of `UserTravelInventoryResponse`.
    """

    travelinventory: UserTravelInventory

    @staticmethod
    def parse(data):
        return UserTravelInventoryResponse(
            travelinventory=BaseSchema.parse(
                data.get("travelinventory"), UserTravelInventory
            ),
        )
