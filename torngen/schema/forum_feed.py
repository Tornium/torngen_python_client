import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_feed_type_enum import ForumFeedTypeEnum
from .forum_post_id import ForumPostId
from .forum_thread_author import ForumThreadAuthor
from .forum_thread_id import ForumThreadId


@dataclass
class ForumFeed(BaseSchema):
    """
    JSON object of `ForumFeed`.
    """

    user: ForumThreadAuthor
    type: ForumFeedTypeEnum
    title: str
    timestamp: int
    thread_id: ForumThreadId
    text: str
    post_id: ForumPostId
    is_seen: bool

    @staticmethod
    def parse(data):
        return ForumFeed(
            user=BaseSchema.parse(data.get("user"), ForumThreadAuthor),
            type=BaseSchema.parse(data.get("type"), ForumFeedTypeEnum),
            title=BaseSchema.parse(data.get("title"), str),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            thread_id=BaseSchema.parse(data.get("thread_id"), ForumThreadId),
            text=BaseSchema.parse(data.get("text"), str),
            post_id=BaseSchema.parse(data.get("post_id"), ForumPostId),
            is_seen=BaseSchema.parse(data.get("is_seen"), bool),
        )
