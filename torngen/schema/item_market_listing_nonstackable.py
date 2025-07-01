import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_market_listing_item_details import ItemMarketListingItemDetails


@dataclass
class ItemMarketListingNonstackable(BaseSchema):
    """
    JSON object of `ItemMarketListingNonstackable`.
    """

    price: int
    item_details: ItemMarketListingItemDetails
    amount: int

    @staticmethod
    def parse(data):
        return ItemMarketListingNonstackable(
            price=BaseSchema.parse(data.get("price"), int),
            item_details=BaseSchema.parse(
                data.get("item_details"), ItemMarketListingItemDetails
            ),
            amount=BaseSchema.parse(data.get("amount"), int),
        )
