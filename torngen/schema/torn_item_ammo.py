import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .ammo_id import AmmoId
from .torn_item_ammo_type_enum import TornItemAmmoTypeEnum


@dataclass
class TornItemAmmo(BaseSchema):
    """
    JSON object of `TornItemAmmo`.
    """

    types: typing.List[TornItemAmmoTypeEnum]
    price: int
    name: str
    id: AmmoId

    @staticmethod
    def parse(data):
        return TornItemAmmo(
            types=BaseSchema.parse(
                data.get("types"), typing.List[TornItemAmmoTypeEnum]
            ),
            price=BaseSchema.parse(data.get("price"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), AmmoId),
        )
