import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_market_item import ItemMarketItem
from .item_market_listing_nonstackable import ItemMarketListingNonstackable
from .item_market_listing_stackable import ItemMarketListingStackable


@dataclass
class ItemMarket(BaseSchema):
    """
    JSON object of `ItemMarket`.
    """

    listings: typing.List[ItemMarketListingStackable | ItemMarketListingNonstackable]
    item: ItemMarketItem
    cache_timestamp: int

    @staticmethod
    def parse(data):
        return ItemMarket(
            listings=BaseSchema.parse(
                data.get("listings"),
                typing.List[ItemMarketListingStackable | ItemMarketListingNonstackable],
            ),
            item=BaseSchema.parse(data.get("item"), ItemMarketItem),
            cache_timestamp=BaseSchema.parse(data.get("cache_timestamp"), int),
        )
