import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .torn_item_type_enum import TornItemTypeEnum
from .torn_item_weapon_type_enum import TornItemWeaponTypeEnum


@dataclass
class MissionRewardDetailsItem(BaseSchema):
    """
    JSON object of `MissionRewardDetailsItem`.
    """

    type: TornItemTypeEnum
    sub_type: None | TornItemWeaponTypeEnum
    name: str
    id: ItemId

    @staticmethod
    def parse(data):
        return MissionRewardDetailsItem(
            type=BaseSchema.parse(data.get("type"), TornItemTypeEnum),
            sub_type=BaseSchema.parse(
                data.get("sub_type"), None | TornItemWeaponTypeEnum
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )
