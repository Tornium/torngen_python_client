import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .trade_id import TradeId
from .user_trade_participant import UserTradeParticipant


@dataclass
class UserTrade(BaseSchema):
    """
    JSON object of `UserTrade`.
    """

    user: UserTradeParticipant
    trader: UserTradeParticipant
    timestamp: int
    id: TradeId

    @staticmethod
    def parse(data):
        return UserTrade(
            user=BaseSchema.parse(data.get("user"), UserTradeParticipant),
            trader=BaseSchema.parse(data.get("trader"), UserTradeParticipant),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), TradeId),
        )
