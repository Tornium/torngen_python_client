import typing

from ..base_schema import BaseSchema
from .forum_poll import ForumPoll
from .forum_thread_base import ForumThreadBase


class ForumThreadExtended(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "", {"poll": None | ForumPoll, "content_raw": str, "content": str}
        )
        | ForumThreadBase
    ]
