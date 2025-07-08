import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_market_listing_item_bonus import ItemMarketListingItemBonus
from .item_market_listing_item_stats import ItemMarketListingItemStats
from .item_uid import ItemUid


@dataclass
class UserItemMarkeListingItemDetails(BaseSchema):
    """
    JSON object of `UserItemMarkeListingItemDetails`.
    """

    uid: None | ItemUid
    type: str
    stats: None | ItemMarketListingItemStats
    rarity: None | typing.Literal["yellow", "orange", "red"]
    name: str
    id: int
    bonuses: typing.List[ItemMarketListingItemBonus]

    @staticmethod
    def parse(data):
        return UserItemMarkeListingItemDetails(
            uid=BaseSchema.parse(data.get("uid"), None | ItemUid),
            type=BaseSchema.parse(data.get("type"), str),
            stats=BaseSchema.parse(
                data.get("stats"), None | ItemMarketListingItemStats
            ),
            rarity=BaseSchema.parse(
                data.get("rarity"), None | typing.Literal["yellow", "orange", "red"]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), int),
            bonuses=BaseSchema.parse(
                data.get("bonuses"), typing.List[ItemMarketListingItemBonus]
            ),
        )
