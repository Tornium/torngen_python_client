import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_market_listing_item_bonus import ItemMarketListingItemBonus
from .item_market_listing_item_stats import ItemMarketListingItemStats
from .item_uid import ItemUid


@dataclass
class ItemMarketListingItemDetails(BaseSchema):
    """
    JSON object of `ItemMarketListingItemDetails`.
    """

    uid: ItemUid
    stats: ItemMarketListingItemStats
    rarity: None | str
    bonuses: typing.List[ItemMarketListingItemBonus]

    @staticmethod
    def parse(data):
        return ItemMarketListingItemDetails(
            uid=BaseSchema.parse(data.get("uid"), ItemUid),
            stats=BaseSchema.parse(data.get("stats"), ItemMarketListingItemStats),
            rarity=BaseSchema.parse(data.get("rarity"), None | str),
            bonuses=BaseSchema.parse(
                data.get("bonuses"), typing.List[ItemMarketListingItemBonus]
            ),
        )
