import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class UserTradeParticipant(BaseSchema):
    """
    JSON object of `UserTradeParticipant`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return UserTradeParticipant(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
