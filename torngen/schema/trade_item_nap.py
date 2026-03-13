import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_faction_basic import UserFactionBasic
from .user_id import UserId


@dataclass
class TradeItemNap(BaseSchema):
    """
    JSON object of `TradeItemNap`.
    """

    user_id: UserId
    type: typing.Literal["NAP"]
    details: typing.TypedDict(
        "", {"factions": typing.List[UserFactionBasic], "days": int}
    )

    @staticmethod
    def parse(data):
        return TradeItemNap(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["NAP"]),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict(
                    "", {"factions": typing.List[UserFactionBasic], "days": int}
                ),
            ),
        )
