import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid
from .user_id import UserId


@dataclass
class TradeItemItem(BaseSchema):
    """
    JSON object of `TradeItemItem`.
    """

    user_id: UserId
    type: typing.Literal["Item"]
    details: typing.TypedDict("", {"uid": None | ItemUid, "id": ItemId, "amount": int})

    @staticmethod
    def parse(data):
        return TradeItemItem(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["Item"]),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict(
                    "", {"uid": None | ItemUid, "id": ItemId, "amount": int}
                ),
            ),
        )
