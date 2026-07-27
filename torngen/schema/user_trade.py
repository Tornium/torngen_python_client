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
    timestamp: typing.Optional[int]
    modified_at: None | int
    id: TradeId
    expires_at: None | int
    completed_at: None | int

    @staticmethod
    def parse(data):
        return UserTrade(
            user=BaseSchema.parse(data.get("user"), UserTradeParticipant),
            trader=BaseSchema.parse(data.get("trader"), UserTradeParticipant),
            timestamp=BaseSchema.parse(data.get("timestamp"), typing.Optional[int]),
            modified_at=BaseSchema.parse(data.get("modified_at"), None | int),
            id=BaseSchema.parse(data.get("id"), TradeId),
            expires_at=BaseSchema.parse(data.get("expires_at"), None | int),
            completed_at=BaseSchema.parse(data.get("completed_at"), None | int),
        )
