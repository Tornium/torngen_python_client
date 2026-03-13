import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_trade_detailed import UserTradeDetailed


@dataclass
class UserTradeResponse(BaseSchema):
    """
    JSON object of `UserTradeResponse`.
    """

    trade: UserTradeDetailed

    @staticmethod
    def parse(data):
        return UserTradeResponse(
            trade=BaseSchema.parse(data.get("trade"), UserTradeDetailed),
        )
