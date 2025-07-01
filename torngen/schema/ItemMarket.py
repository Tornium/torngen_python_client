import typing

from ItemMarketItem import ItemMarketItem
from ItemMarketListingNonstackable import ItemMarketListingNonstackable
from ItemMarketListingStackable import ItemMarketListingStackable

from ..base_schema import BaseSchema


class ItemMarket(BaseSchema):

    listings: typing.List[ItemMarketListingStackable | ItemMarketListingNonstackable]
    item: ItemMarketItem
    cache_timestamp: int
