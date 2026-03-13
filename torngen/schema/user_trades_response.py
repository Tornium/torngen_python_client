import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_trade import UserTrade


@dataclass
class UserTradesResponse(BaseSchema):
    """
    JSON object of `UserTradesResponse`.
    """

    trades: typing.List[UserTrade]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserTradesResponse(
            trades=BaseSchema.parse(data.get("trades"), typing.List[UserTrade]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )
