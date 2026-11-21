import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .auction_house_listing import AuctionHouseListing
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class AuctionHouseResponse(BaseSchema):
    """
    JSON object of `AuctionHouseResponse`.
    """

    auctionhouse_timestamp: typing.Optional[int]
    auctionhouse_delay: typing.Optional[int]
    auctionhouse: typing.List[AuctionHouseListing]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return AuctionHouseResponse(
            auctionhouse_timestamp=BaseSchema.parse(
                data.get("auctionhouse_timestamp"), typing.Optional[int]
            ),
            auctionhouse_delay=BaseSchema.parse(
                data.get("auctionhouse_delay"), typing.Optional[int]
            ),
            auctionhouse=BaseSchema.parse(
                data.get("auctionhouse"), typing.List[AuctionHouseListing]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
