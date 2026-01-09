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

    auctionhouse: typing.List[AuctionHouseListing]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return AuctionHouseResponse(
            auctionhouse=BaseSchema.parse(
                data.get("auctionhouse"), typing.List[AuctionHouseListing]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
