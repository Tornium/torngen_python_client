import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .property_id import PropertyId
from .user_id import UserId


@dataclass
class TradeItemProperty(BaseSchema):
    """
    JSON object of `TradeItemProperty`.
    """

    user_id: UserId
    type: typing.Literal["Property"]
    details: typing.TypedDict("", {"id": PropertyId, "happiness": int})

    @staticmethod
    def parse(data):
        return TradeItemProperty(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["Property"]),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict("", {"id": PropertyId, "happiness": int}),
            ),
        )
