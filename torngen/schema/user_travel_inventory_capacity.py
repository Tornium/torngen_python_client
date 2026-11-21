import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserTravelInventoryCapacity(BaseSchema):
    """
    JSON object of `UserTravelInventoryCapacity`.
    """

    special: int
    base: int

    @staticmethod
    def parse(data):
        return UserTravelInventoryCapacity(
            special=BaseSchema.parse(data.get("special"), int),
            base=BaseSchema.parse(data.get("base"), int),
        )
