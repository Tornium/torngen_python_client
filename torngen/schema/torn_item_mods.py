import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_mod_id import ItemModId
from .torn_item_weapon_type_enum import TornItemWeaponTypeEnum


@dataclass
class TornItemMods(BaseSchema):
    """
    JSON object of `TornItemMods`.
    """

    weapons: typing.List[TornItemWeaponTypeEnum]
    name: str
    id: ItemModId
    dual_fit: bool
    description: str

    @staticmethod
    def parse(data):
        return TornItemMods(
            weapons=BaseSchema.parse(
                data.get("weapons"), typing.List[TornItemWeaponTypeEnum]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemModId),
            dual_fit=BaseSchema.parse(data.get("dual_fit"), bool),
            description=BaseSchema.parse(data.get("description"), str),
        )
