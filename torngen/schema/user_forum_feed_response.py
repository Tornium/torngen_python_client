import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_feed import ForumFeed


@dataclass
class UserForumFeedResponse(BaseSchema):
    """
    JSON object of `UserForumFeedResponse`.
    """

    forumFeed: typing.List[ForumFeed]

    @staticmethod
    def parse(data):
        return UserForumFeedResponse(
            forumFeed=BaseSchema.parse(data.get("forumFeed"), typing.List[ForumFeed]),
        )
