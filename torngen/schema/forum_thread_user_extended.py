import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_id import ForumId
from .forum_thread_author import ForumThreadAuthor
from .forum_thread_id import ForumThreadId


@dataclass
class ForumThreadUserExtended(BaseSchema):

    new_posts: None | int
    views: int
    title: str
    rating: int
    posts: int
    last_poster: None | ForumThreadAuthor
    last_post_time: None | int
    is_sticky: bool
    is_locked: bool
    id: ForumThreadId
    has_poll: bool
    forum_id: ForumId
    first_post_time: int
    author: ForumThreadAuthor

    @staticmethod
    def parse(data):
        return ForumThreadUserExtended(
            new_posts=BaseSchema.parse(data.get("new_posts"), None | int),
            views=BaseSchema.parse(data.get("views"), int),
            title=BaseSchema.parse(data.get("title"), str),
            rating=BaseSchema.parse(data.get("rating"), int),
            posts=BaseSchema.parse(data.get("posts"), int),
            last_poster=BaseSchema.parse(
                data.get("last_poster"), None | ForumThreadAuthor
            ),
            last_post_time=BaseSchema.parse(data.get("last_post_time"), None | int),
            is_sticky=BaseSchema.parse(data.get("is_sticky"), bool),
            is_locked=BaseSchema.parse(data.get("is_locked"), bool),
            id=BaseSchema.parse(data.get("id"), ForumThreadId),
            has_poll=BaseSchema.parse(data.get("has_poll"), bool),
            forum_id=BaseSchema.parse(data.get("forum_id"), ForumId),
            first_post_time=BaseSchema.parse(data.get("first_post_time"), int),
            author=BaseSchema.parse(data.get("author"), ForumThreadAuthor),
        )
