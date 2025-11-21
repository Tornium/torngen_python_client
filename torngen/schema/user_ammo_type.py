import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_ammo_type_enum import TornItemAmmoTypeEnum


@dataclass
class UserAmmoType(BaseSchema):
    """
    JSON object of `UserAmmoType`.
    """

    quantity: int
    name: TornItemAmmoTypeEnum
    equipped: bool

    @staticmethod
    def parse(data):
        return UserAmmoType(
            quantity=BaseSchema.parse(data.get("quantity"), int),
            name=BaseSchema.parse(data.get("name"), TornItemAmmoTypeEnum),
            equipped=BaseSchema.parse(data.get("equipped"), bool),
        )
