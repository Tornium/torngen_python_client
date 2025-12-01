import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_market_listing_item_bonus import ItemMarketListingItemBonus
from .item_market_listing_item_stats import ItemMarketListingItemStats
from .item_uid import ItemUid
from .torn_item_type_enum import TornItemTypeEnum
from .torn_item_weapon_type_enum import TornItemWeaponTypeEnum


@dataclass
class UserEquipment(BaseSchema):

    slot: int

    @staticmethod
    def parse(data):
        return UserEquipment(
            slot=BaseSchema.parse(data.get("slot"), int),
        )
