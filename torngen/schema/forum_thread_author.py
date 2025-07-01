import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class ForumThreadAuthor(BaseSchema):
    """
    JSON object of `ForumThreadAuthor`.
    """

    username: str
    karma: int
    id: UserId

    @staticmethod
    def parse(data):
        return ForumThreadAuthor(
            username=BaseSchema.parse(data.get("username"), str),
            karma=BaseSchema.parse(data.get("karma"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
