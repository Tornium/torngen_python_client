import typing

from ItemMarketListingItemDetails import ItemMarketListingItemDetails

from ..base_schema import BaseSchema


class ItemMarketListingNonstackable(BaseSchema):

    price: int
    item_details: ItemMarketListingItemDetails
    amount: int
