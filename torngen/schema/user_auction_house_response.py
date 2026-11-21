import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_auction_house_listing import UserAuctionHouseListing


@dataclass
class UserAuctionHouseResponse(BaseSchema):
    """
    JSON object of `UserAuctionHouseResponse`.
    """

    auctionhouse: typing.List[UserAuctionHouseListing]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserAuctionHouseResponse(
            auctionhouse=BaseSchema.parse(
                data.get("auctionhouse"), typing.List[UserAuctionHouseListing]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
