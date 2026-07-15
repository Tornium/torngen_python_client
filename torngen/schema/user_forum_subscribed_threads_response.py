import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_subscribed_thread import ForumSubscribedThread


@dataclass
class UserForumSubscribedThreadsResponse(BaseSchema):
    """
    JSON object of `UserForumSubscribedThreadsResponse`.
    """

    forumSubscribedThreads: typing.List[ForumSubscribedThread]

    @staticmethod
    def parse(data):
        return UserForumSubscribedThreadsResponse(
            forumSubscribedThreads=BaseSchema.parse(
                data.get("forumSubscribedThreads"), typing.List[ForumSubscribedThread]
            ),
        )
