import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .ammo_id import AmmoId
from .torn_item_ammo_type_enum import TornItemAmmoTypeEnum


@dataclass
class MissionRewardDetailsAmmo(BaseSchema):
    """
    JSON object of `MissionRewardDetailsAmmo`.
    """

    type: TornItemAmmoTypeEnum
    name: str
    id: AmmoId

    @staticmethod
    def parse(data):
        return MissionRewardDetailsAmmo(
            type=BaseSchema.parse(data.get("type"), TornItemAmmoTypeEnum),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), AmmoId),
        )
