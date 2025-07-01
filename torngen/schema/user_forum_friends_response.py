import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_feed import ForumFeed


@dataclass
class UserForumFriendsResponse(BaseSchema):
    """
    JSON object of `UserForumFriendsResponse`.
    """

    forumFriends: typing.List[ForumFeed]

    @staticmethod
    def parse(data):
        return UserForumFriendsResponse(
            forumFriends=BaseSchema.parse(
                data.get("forumFriends"), typing.List[ForumFeed]
            ),
        )
