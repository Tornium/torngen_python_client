import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_id import ForumId
from .forum_subscribed_thread_posts_count import ForumSubscribedThreadPostsCount
from .forum_thread_author import ForumThreadAuthor
from .forum_thread_id import ForumThreadId


@dataclass
class ForumSubscribedThread(BaseSchema):
    """
    JSON object of `ForumSubscribedThread`.
    """

    title: str
    posts: ForumSubscribedThreadPostsCount
    id: ForumThreadId
    forum_id: ForumId
    author: ForumThreadAuthor

    @staticmethod
    def parse(data):
        return ForumSubscribedThread(
            title=BaseSchema.parse(data.get("title"), str),
            posts=BaseSchema.parse(data.get("posts"), ForumSubscribedThreadPostsCount),
            id=BaseSchema.parse(data.get("id"), ForumThreadId),
            forum_id=BaseSchema.parse(data.get("forum_id"), ForumId),
            author=BaseSchema.parse(data.get("author"), ForumThreadAuthor),
        )
