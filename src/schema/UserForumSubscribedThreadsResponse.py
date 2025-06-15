import typing

from ForumSubscribedThread import ForumSubscribedThread

from ..base_schema import BaseSchema


class UserForumSubscribedThreadsResponse(BaseSchema):

    forumSubscribedThreads: typing.List[ForumSubscribedThread]
