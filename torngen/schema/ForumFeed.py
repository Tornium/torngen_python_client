import typing

from ForumFeedTypeEnum import ForumFeedTypeEnum
from ForumPostId import ForumPostId
from ForumThreadAuthor import ForumThreadAuthor
from ForumThreadId import ForumThreadId

from ..base_schema import BaseSchema


class ForumFeed(BaseSchema):

    user: ForumThreadAuthor
    type: ForumFeedTypeEnum
    title: str
    timestamp: int
    thread_id: ForumThreadId
    text: str
    post_id: ForumPostId
    is_seen: bool
