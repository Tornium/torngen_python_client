import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .auction_house_stackable_item import AuctionHouseStackableItem
from .auction_listing_id import AuctionListingId
from .basic_user import BasicUser
from .torn_item_details import TornItemDetails


@dataclass
class UserAuctionHouseListing(BaseSchema):
    """
    JSON object of `UserAuctionHouseListing`.
    """

    timestamp: int
    price: int
    item: TornItemDetails | AuctionHouseStackableItem
    id: AuctionListingId
    buyer: BasicUser
    bids: int

    @staticmethod
    def parse(data):
        return UserAuctionHouseListing(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            price=BaseSchema.parse(data.get("price"), int),
            item=BaseSchema.parse(
                data.get("item"), TornItemDetails | AuctionHouseStackableItem
            ),
            id=BaseSchema.parse(data.get("id"), AuctionListingId),
            buyer=BaseSchema.parse(data.get("buyer"), BasicUser),
            bids=BaseSchema.parse(data.get("bids"), int),
        )
