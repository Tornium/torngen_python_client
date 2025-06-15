import typing

from ForumFeed import ForumFeed

from ..base_schema import BaseSchema


class UserForumFeedResponse(BaseSchema):

    forumFeed: typing.List[ForumFeed]
