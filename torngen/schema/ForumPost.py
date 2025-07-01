import typing

from ForumPostId import ForumPostId
from ForumThreadAuthor import ForumThreadAuthor
from ForumThreadId import ForumThreadId
from UserId import UserId

from ..base_schema import BaseSchema


class ForumPost(BaseSchema):

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
