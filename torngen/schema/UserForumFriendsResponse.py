import typing

from ForumFeed import ForumFeed

from ..base_schema import BaseSchema


class UserForumFriendsResponse(BaseSchema):

    forumFriends: typing.List[ForumFeed]
