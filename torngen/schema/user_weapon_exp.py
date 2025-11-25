import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class UserWeaponExp(BaseSchema):
    """
    JSON object of `UserWeaponExp`.
    """

    name: str
    id: ItemId
    exp: int

    @staticmethod
    def parse(data):
        return UserWeaponExp(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
            exp=BaseSchema.parse(data.get("exp"), int),
        )
