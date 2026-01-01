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
    type: TornItemTypeEnum
    sub_type: None | TornItemWeaponTypeEnum
    name: str
    id: ItemId
    uid: ItemUid
    stats: ItemMarketListingItemStats
    rarity: None | typing.Literal["yellow", "orange", "red"]
    bonuses: typing.List[ItemMarketListingItemBonus]

    @staticmethod
    def parse(data):
        return UserEquipment(
            slot=BaseSchema.parse(data.get("slot"), int),
            type=BaseSchema.parse(data.get("type"), TornItemTypeEnum),
            sub_type=BaseSchema.parse(
                data.get("sub_type"), None | TornItemWeaponTypeEnum
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
            uid=BaseSchema.parse(data.get("uid"), ItemUid),
            stats=BaseSchema.parse(data.get("stats"), ItemMarketListingItemStats),
            rarity=BaseSchema.parse(
                data.get("rarity"), None | typing.Literal["yellow", "orange", "red"]
            ),
            bonuses=BaseSchema.parse(
                data.get("bonuses"), typing.List[ItemMarketListingItemBonus]
            ),
        )
