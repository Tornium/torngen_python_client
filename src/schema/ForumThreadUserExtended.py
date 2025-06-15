import typing

from ForumThreadBase import ForumThreadBase

from ..base_schema import BaseSchema


class ForumThreadUserExtended(BaseSchema):
    value: typing.List[
        typing.TypedDict("", {"new_posts": None | int}) | ForumThreadBase
    ]
