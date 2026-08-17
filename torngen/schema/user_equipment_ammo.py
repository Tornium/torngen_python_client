import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .ammo_id import AmmoId
from .torn_item_ammo_type_enum import TornItemAmmoTypeEnum


@dataclass
class UserEquipmentAmmo(BaseSchema):
    """
    JSON object of `UserEquipmentAmmo`.
    """

    type: TornItemAmmoTypeEnum
    quantity: int
    name: str
    id: AmmoId

    @staticmethod
    def parse(data):
        return UserEquipmentAmmo(
            type=BaseSchema.parse(data.get("type"), TornItemAmmoTypeEnum),
            quantity=BaseSchema.parse(data.get("quantity"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), AmmoId),
        )
