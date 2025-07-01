import typing

from ForumThreadExtended import ForumThreadExtended

from ..base_schema import BaseSchema


class ForumThreadResponse(BaseSchema):

    thread: ForumThreadExtended
