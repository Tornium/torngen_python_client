import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .auction_house_listing import AuctionHouseListing


@dataclass
class AuctionHouseListingResponse(BaseSchema):
    """
    JSON object of `AuctionHouseListingResponse`.
    """

    auctionhouselisting: AuctionHouseListing

    @staticmethod
    def parse(data):
        return AuctionHouseListingResponse(
            auctionhouselisting=BaseSchema.parse(
                data.get("auctionhouselisting"), AuctionHouseListing
            ),
        )
