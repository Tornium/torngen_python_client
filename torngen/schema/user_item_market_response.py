import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_item_market_listing import UserItemMarketListing


@dataclass
class UserItemMarketResponse(BaseSchema):
    """
    JSON object of `UserItemMarketResponse`.
    """

    itemmarket: typing.List[UserItemMarketListing]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserItemMarketResponse(
            itemmarket=BaseSchema.parse(
                data.get("itemmarket"), typing.List[UserItemMarketListing]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
