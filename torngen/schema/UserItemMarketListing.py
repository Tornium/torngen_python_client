import typing

from UserItemMarkeListingItemDetails import UserItemMarkeListingItemDetails

from ..base_schema import BaseSchema


class UserItemMarketListing(BaseSchema):

    price: int
    item: UserItemMarkeListingItemDetails
    is_anonymous: bool
    id: int
    average_price: int
    available: int
    amount: int
