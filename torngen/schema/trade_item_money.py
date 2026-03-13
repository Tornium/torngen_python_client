import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class TradeItemMoney(BaseSchema):
    """
    JSON object of `TradeItemMoney`.
    """

    user_id: UserId
    type: typing.Literal["Money"]
    details: typing.TypedDict("", {"amount": int})

    @staticmethod
    def parse(data):
        return TradeItemMoney(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["Money"]),
            details=BaseSchema.parse(
                data.get("details"), typing.TypedDict("", {"amount": int})
            ),
        )
