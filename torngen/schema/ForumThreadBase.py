import typing

from ForumId import ForumId
from ForumThreadAuthor import ForumThreadAuthor
from ForumThreadId import ForumThreadId

from ..base_schema import BaseSchema


class ForumThreadBase(BaseSchema):

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
