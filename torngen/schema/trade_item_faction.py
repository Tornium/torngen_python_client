import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_id import UserId


@dataclass
class TradeItemFaction(BaseSchema):
    """
    JSON object of `TradeItemFaction`.
    """

    user_id: UserId
    type: typing.Literal["Faction"]
    details: typing.TypedDict("", {"respect": int, "name": str, "id": FactionId})

    @staticmethod
    def parse(data):
        return TradeItemFaction(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["Faction"]),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict("", {"respect": int, "name": str, "id": FactionId}),
            ),
        )
