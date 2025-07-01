import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_item_marke_listing_item_details import \
    UserItemMarkeListingItemDetails


@dataclass
class UserItemMarketListing(BaseSchema):
    """
    JSON object of `UserItemMarketListing`.
    """

    price: int
    item: UserItemMarkeListingItemDetails
    is_anonymous: bool
    id: int
    average_price: int
    available: int
    amount: int

    @staticmethod
    def parse(data):
        return UserItemMarketListing(
            price=BaseSchema.parse(data.get("price"), int),
            item=BaseSchema.parse(data.get("item"), UserItemMarkeListingItemDetails),
            is_anonymous=BaseSchema.parse(data.get("is_anonymous"), bool),
            id=BaseSchema.parse(data.get("id"), int),
            average_price=BaseSchema.parse(data.get("average_price"), int),
            available=BaseSchema.parse(data.get("available"), int),
            amount=BaseSchema.parse(data.get("amount"), int),
        )
