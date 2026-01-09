import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .auction_house_stackable_item import AuctionHouseStackableItem
from .auction_listing_id import AuctionListingId
from .basic_user import BasicUser
from .torn_item_details import TornItemDetails


@dataclass
class AuctionHouseListing(BaseSchema):
    """
    JSON object of `AuctionHouseListing`.
    """

    timestamp: int
    seller: BasicUser
    price: int
    item: TornItemDetails | AuctionHouseStackableItem
    id: AuctionListingId
    buyer: BasicUser
    bids: int

    @staticmethod
    def parse(data):
        return AuctionHouseListing(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            seller=BaseSchema.parse(data.get("seller"), BasicUser),
            price=BaseSchema.parse(data.get("price"), int),
            item=BaseSchema.parse(
                data.get("item"), TornItemDetails | AuctionHouseStackableItem
            ),
            id=BaseSchema.parse(data.get("id"), AuctionListingId),
            buyer=BaseSchema.parse(data.get("buyer"), BasicUser),
            bids=BaseSchema.parse(data.get("bids"), int),
        )
