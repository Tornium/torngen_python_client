import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_ammo import TornItemAmmo


@dataclass
class TornItemAmmoResponse(BaseSchema):
    """
    JSON object of `TornItemAmmoResponse`.
    """

    itemammo: typing.List[TornItemAmmo]

    @staticmethod
    def parse(data):
        return TornItemAmmoResponse(
            itemammo=BaseSchema.parse(data.get("itemammo"), typing.List[TornItemAmmo]),
        )
