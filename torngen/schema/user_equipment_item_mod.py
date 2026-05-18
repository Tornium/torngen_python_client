import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_mod_id import ItemModId


@dataclass
class UserEquipmentItemMod(BaseSchema):
    """
    JSON object of `UserEquipmentItemMod`.
    """

    name: str
    id: ItemModId

    @staticmethod
    def parse(data):
        return UserEquipmentItemMod(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemModId),
        )
