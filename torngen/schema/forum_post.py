import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_post_id import ForumPostId
from .forum_thread_author import ForumThreadAuthor
from .forum_thread_id import ForumThreadId
from .user_id import UserId


@dataclass
class ForumPost(BaseSchema):
    """
    JSON object of `ForumPost`.
    """

    thread_id: ForumThreadId
    quoted_post_id: None | int
    likes: int
    is_topic: bool
    is_pinned: bool
    is_legacy: bool
    is_edited: bool
    id: ForumPostId
    has_quote: bool
    edited_by: None | UserId
    dislikes: int
    created_time: int
    content: str
    author: ForumThreadAuthor

    @staticmethod
    def parse(data):
        return ForumPost(
            thread_id=BaseSchema.parse(data.get("thread_id"), ForumThreadId),
            quoted_post_id=BaseSchema.parse(data.get("quoted_post_id"), None | int),
            likes=BaseSchema.parse(data.get("likes"), int),
            is_topic=BaseSchema.parse(data.get("is_topic"), bool),
            is_pinned=BaseSchema.parse(data.get("is_pinned"), bool),
            is_legacy=BaseSchema.parse(data.get("is_legacy"), bool),
            is_edited=BaseSchema.parse(data.get("is_edited"), bool),
            id=BaseSchema.parse(data.get("id"), ForumPostId),
            has_quote=BaseSchema.parse(data.get("has_quote"), bool),
            edited_by=BaseSchema.parse(data.get("edited_by"), None | UserId),
            dislikes=BaseSchema.parse(data.get("dislikes"), int),
            created_time=BaseSchema.parse(data.get("created_time"), int),
            content=BaseSchema.parse(data.get("content"), str),
            author=BaseSchema.parse(data.get("author"), ForumThreadAuthor),
        )
