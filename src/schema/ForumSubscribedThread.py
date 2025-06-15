import typing

from ForumId import ForumId
from ForumSubscribedThreadPostsCount import ForumSubscribedThreadPostsCount
from ForumThreadAuthor import ForumThreadAuthor
from ForumThreadId import ForumThreadId

from ..base_schema import BaseSchema


class ForumSubscribedThread(BaseSchema):

    title: str
    posts: ForumSubscribedThreadPostsCount
    id: ForumThreadId
    forum_id: ForumId
    author: ForumThreadAuthor
