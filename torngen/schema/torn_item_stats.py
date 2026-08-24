import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid
from .torn_item_stat import TornItemStat
from .torn_item_stat_title_enum import TornItemStatTitleEnum
from .torn_item_type_enum import TornItemTypeEnum
from .torn_item_weapon_type_enum import TornItemWeaponTypeEnum


@dataclass
class TornItemStats(BaseSchema):
    """
    JSON object of `TornItemStats`.
    """

    uid: ItemUid
    type: TornItemTypeEnum
    sub_type: None | TornItemWeaponTypeEnum
    stats: typing.List[TornItemStat]
    name: TornItemStatTitleEnum
    id: ItemId

    @staticmethod
    def parse(data):
        return TornItemStats(
            uid=BaseSchema.parse(data.get("uid"), ItemUid),
            type=BaseSchema.parse(data.get("type"), TornItemTypeEnum),
            sub_type=BaseSchema.parse(
                data.get("sub_type"), None | TornItemWeaponTypeEnum
            ),
            stats=BaseSchema.parse(data.get("stats"), typing.List[TornItemStat]),
            name=BaseSchema.parse(data.get("name"), TornItemStatTitleEnum),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )
