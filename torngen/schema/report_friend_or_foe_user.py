import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class ReportFriendOrFoeUser(BaseSchema):
    """
    JSON object of `ReportFriendOrFoeUser`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return ReportFriendOrFoeUser(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
