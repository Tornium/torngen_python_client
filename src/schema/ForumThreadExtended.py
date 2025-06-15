import typing

from ForumPoll import ForumPoll
from ForumThreadBase import ForumThreadBase

from ..base_schema import BaseSchema


class ForumThreadExtended(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "", {"poll": None | ForumPoll, "content_raw": str, "content": str}
        )
        | ForumThreadBase
    ]
