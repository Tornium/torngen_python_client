import typing

from ..base_schema import BaseSchema
from .forum_thread_base import ForumThreadBase


class ForumThreadUserExtended(BaseSchema):
    value: typing.List[
        typing.TypedDict("", {"new_posts": None | int}) | ForumThreadBase
    ]
