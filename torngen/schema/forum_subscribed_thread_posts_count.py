import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ForumSubscribedThreadPostsCount(BaseSchema):
    """
    JSON object of `ForumSubscribedThreadPostsCount`.
    """

    total: int
    new: int

    @staticmethod
    def parse(data):
        return ForumSubscribedThreadPostsCount(
            total=BaseSchema.parse(data.get("total"), int),
            new=BaseSchema.parse(data.get("new"), int),
        )
