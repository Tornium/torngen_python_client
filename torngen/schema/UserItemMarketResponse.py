import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from UserItemMarketListing import UserItemMarketListing

from ..base_schema import BaseSchema


class UserItemMarketResponse(BaseSchema):

    itemmarket: typing.List[UserItemMarketListing]
    _metadata: RequestMetadataWithLinks
