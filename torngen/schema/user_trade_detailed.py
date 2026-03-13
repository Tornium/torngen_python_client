import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .trade_id import TradeId
from .trade_item import TradeItem
from .user_trade_participant import UserTradeParticipant


@dataclass
class UserTradeDetailed(BaseSchema):

    items: typing.List[TradeItem]
    user: UserTradeParticipant
    trader: UserTradeParticipant
    timestamp: int
    id: TradeId

    @staticmethod
    def parse(data):
        return UserTradeDetailed(
            items=BaseSchema.parse(data.get("items"), typing.List[TradeItem]),
            user=BaseSchema.parse(data.get("user"), UserTradeParticipant),
            trader=BaseSchema.parse(data.get("trader"), UserTradeParticipant),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), TradeId),
        )
